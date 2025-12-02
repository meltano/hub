"""PluginSchemaValidator class."""

import json
import logging
import os
import sys
from pathlib import Path

from jsonschema import Draft7Validator
from referencing import Registry, Resource
from referencing.jsonschema import DRAFT7
from ruamel.yaml import YAML

logging.basicConfig(level=logging.INFO, stream=sys.stdout)
logger = logging.getLogger(os.path.basename(__file__))


class PluginSchemaValidator:
    """Validates the Meltano plugin definition content."""

    def __init__(self, file_path="_data/meltano/"):
        """Initialize PluginSchemaValidator.

        Args:
            file_path: Path to Meltano plugin definition files. Defaults to "plugins/".
        """
        self.file_path = file_path
        self._set_schema_store()
        self.yaml = YAML()
        self.all_valid = True
        self.validation_results = {}

    def _set_schema_store(self, schemas_dir="plugin_definitions"):
        resources = []
        for source in Path("schemas/common").iterdir():
            if not source.name.endswith(".json"):
                # Skip non schema files
                continue
            with open(source) as schema_file:
                schema = json.load(schema_file)
                resource = Resource.from_contents(schema, default_specification=DRAFT7)
                resources.append((schema["$id"], resource))
        for source in Path(f"schemas/{schemas_dir}").iterdir():
            if not source.name.endswith(".json"):
                # Skip non schema files
                continue
            with open(source) as schema_file:
                schema = json.load(schema_file)
                resource = Resource.from_contents(schema, default_specification=DRAFT7)
                resources.append((schema["$id"], resource))
        self.registry = Registry().with_resources(resources)

    def _validate_plugin(self, schema, plugin_category, plugin_name, variant_name):
        with open(
            os.path.join(self.file_path, plugin_category, plugin_name, variant_name),
            "r",
        ) as plugin_file:
            plugin_data = self.yaml.load(plugin_file)
            validator = Draft7Validator(schema, registry=self.registry)
            try:
                validator.validate(plugin_data)
            except Exception as ex:
                logger.info(
                    f"Validation error for {plugin_name}.{variant_name} with message {str(ex)}"
                )
                self.all_valid = False
            return True

    def _read_json_schema(self, schema_name, schemas_dir="plugin_definitions"):
        with open(f"schemas/{schemas_dir}/{schema_name}") as schema:
            return json.load(schema)

    def plugins_validate(self):
        """Iterate plugin defintions and validate against JSON schemas."""
        logger.info("Schema validation started...")
        for plugin_category in os.listdir(self.file_path):
            if plugin_category.startswith("."):
                # Skip non plugin definition files
                continue
            logger.info(f"Validating schema for plugin type: {plugin_category}")
            schema = self._read_json_schema(f"{plugin_category}.schema.json")
            plugin_count = 0
            variant_count = 0
            for plugin_name in os.listdir(
                os.path.join(self.file_path, plugin_category)
            ):
                if plugin_name.startswith("."):
                    # Skip non plugin definition files
                    continue
                for variant_name in os.listdir(
                    os.path.join(self.file_path, plugin_category, plugin_name)
                ):
                    if not self._validate_plugin(
                        schema, plugin_category, plugin_name, variant_name
                    ):
                        # dont increment count
                        continue
                    variant_count += 1
                plugin_count += 1
            self.validation_results[plugin_category] = (
                f"Plugins: {plugin_count}, Variants: {variant_count}"
            )


if __name__ == "__main__":
    # accept file path as optional argument
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        validate = PluginSchemaValidator(file_path=file_path)
    else:
        validate = PluginSchemaValidator()
    validate.plugins_validate()

    logger.info("Plugin schema validation complete.")
    if validate.all_valid:
        logger.info("All plugins pass the JSON Schema.")
        logger.info(json.dumps(validate.validation_results, indent=4, sort_keys=True))
        sys.exit()
    else:
        logger.info("Schema validation failed.")
        logger.info(validate.validation_results)
        sys.exit(1)
