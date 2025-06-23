"""APIValidator class."""

import json
import logging
import os
import sys
from pathlib import Path

from jsonschema import Draft7Validator, RefResolver
from ruamel.yaml import YAML

logging.basicConfig(level=logging.INFO, stream=sys.stdout)
logger = logging.getLogger(os.path.basename(__file__))


class APIValidator:
    """Validates the Meltano plugin API content."""

    def __init__(self, file_path="_hub_api/plugins/"):
        """Initialize APIValidator.

        Args:
            file_path: Path to Meltano API files. Defaults to "_hub_api/plugins/".
        """
        self.file_path = file_path
        self._set_schema_store()
        self.yaml = YAML()
        self.all_valid = True
        self.validation_results = {}

    def _set_schema_store(self, schemas_dir="api"):
        self.schema_store = {}
        for source in Path("schemas/common").iterdir():
            with open(source) as schema_file:
                schema = json.load(schema_file)
                self.schema_store[schema["$id"]] = schema
        # TODO: load all common and API schemas
        for source in Path(f"schemas/{schemas_dir}").iterdir():
            with open(source) as schema_file:
                schema = json.load(schema_file)
                self.schema_store[schema["$id"]] = schema

    def _validate_plugin(self, schema, plugin_dir, file_name):
        with open(
            os.path.join(self.file_path, plugin_dir, file_name), "r"
        ) as plugin_file:
            plugin_data = self.yaml.load(plugin_file)
            resolver = RefResolver.from_schema(schema, store=self.schema_store)
            validator = Draft7Validator(schema, resolver=resolver)
            try:
                validator.validate(plugin_data)
            except Exception as ex:
                logger.info(f"Validation error for {file_name} with message {str(ex)}")
                self.all_valid = False
            return True

    def _read_json_schema(self, schema_name, schemas_dir="api"):
        with open(f"schemas/{schemas_dir}/{schema_name}") as schema:
            return json.load(schema)

    def _validate_index(self, file_path, schema_name):
        schema = self._read_json_schema(schema_name)
        with open(os.path.join(file_path, "index"), "r") as type_index:
            type_index_data = self.yaml.load(type_index)
        resolver = RefResolver.from_schema(schema, store=self.schema_store)
        validator = Draft7Validator(schema, resolver=resolver)
        try:
            validator.validate(type_index_data)
        except Exception as ex:
            logger.info(
                f"Validation error for {file_path}/index with message {str(ex)}"
            )
            self.all_valid = False

    def plugins_validate(self):
        """Iterate API generated plugins and validate against JSON schemas."""
        logger.info("API schema validation started...")
        for plugin_dir in os.listdir(self.file_path):
            if plugin_dir == "index":
                self._validate_index(self.file_path, "plugins_index.schema.json")
                continue
            logger.info(f"Validating API schema for plugin type: {plugin_dir}")
            schema = self._read_json_schema(f"{plugin_dir}.schema.json")
            count = 0
            for file_name in os.listdir(os.path.join(self.file_path, plugin_dir)):
                if file_name == "index":
                    self._validate_index(
                        os.path.join(self.file_path, plugin_dir),
                        "plugin_type_index.schema.json",
                    )
                    continue
                if not self._validate_plugin(schema, plugin_dir, file_name):
                    # dont increment count
                    continue
                count += 1
            self.validation_results[plugin_dir] = count


if __name__ == "__main__":
    # accept file path as optional argument
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        validate = APIValidator(file_path=file_path)
    else:
        validate = APIValidator()
    validate.plugins_validate()

    logger.info("API schema validation complete.")
    if validate.all_valid:
        logger.info("All plugins pass the JSON Schema.")
        logger.info(json.dumps(validate.validation_results, indent=4, sort_keys=True))
        sys.exit()
    else:
        logger.info("Schema validation failed.")
        logger.info(validate.validation_results)
        sys.exit(1)
