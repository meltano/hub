import json
import os
import sys
from pathlib import Path

from jsonschema import Draft7Validator, RefResolver
from ruamel.yaml import YAML


class APIValidator:

    def __init__(self):
        self.file_path = "meltano/api/v1/plugins/"
        # accept file path as optional argument
        if len(sys.argv) > 1:
            self.file_path = sys.argv[1]
        self._set_schema_store()
        self.yaml = YAML()
        self.all_valid = True
        self.validation_results = {}

    def _set_schema_store(self):
        self.schema_store = {}
        for source in Path("schemas").iterdir():
            with open(source) as schema_file:
                schema = json.load(schema_file)
                self.schema_store[schema["$id"]] = schema

    def _validate_plugin(self, schema, plugin_dir, file_name):
        with open(os.path.join(self.file_path, plugin_dir, file_name), "r") as plugin_file:
            plugin_data = self.yaml.load(plugin_file)
            resolver = RefResolver.from_schema(schema, store=self.schema_store)
            validator = Draft7Validator(schema, resolver=resolver)
            try:
                validator.validate(plugin_data)
            except Exception as ex:
                print(
                    f"Validation error for {file_name} with message {str(ex)}")
                self.all_valid = False
            return True

    def _validate_index(self, file_path, schema_name):
        schema = json.load(open(f"schemas/{schema_name}"))
        with open(os.path.join(file_path, "index"), "r") as type_index:
            type_index_data = self.yaml.load(type_index)
        resolver = RefResolver.from_schema(schema, store=self.schema_store)
        validator = Draft7Validator(schema, resolver=resolver)
        try:
            validator.validate(type_index_data)
        except Exception as ex:
            print(
                f"Validation error for {file_path}/index with message {str(ex)}"
            )
            self.all_valid = False

    def plugins_validate(self):
        print("API schema validation started...")
        for plugin_dir in os.listdir(self.file_path):
            if plugin_dir == "index":
                self._validate_index(
                    self.file_path,
                    "plugins_index.schema.json"
                )
                continue
            print(f"Validating API schema for plugin type: {plugin_dir}")
            schema = json.load(open(f"schemas/{plugin_dir}.schema.json"))
            count = 0
            for file_name in os.listdir(os.path.join(self.file_path, plugin_dir)):
                if file_name == "index":
                    self._validate_index(
                        os.path.join(self.file_path, plugin_dir),
                        "plugin_type_index.schema.json"
                    )
                    continue
                if not self._validate_plugin(schema, plugin_dir, file_name):
                    # dont increment count
                    continue
                count += 1
            self.validation_results[plugin_dir] = count


validate = APIValidator()
validate.plugins_validate()

print("API schema validation complete.")
if validate.all_valid:
    print("All plugins pass the JSON Schema.")
    print(json.dumps(validate.validation_results, indent=4, sort_keys=True))
    sys.exit()
else:
    print("Schema validation failed.")
    print(validate.validation_results)
    sys.exit(1)