import json
import os
import sys
from pathlib import Path

from jsonschema import Draft7Validator, RefResolver
from ruamel.yaml import YAML

schemas = (json.load(open(source)) for source in Path(f"schemas").iterdir())
schema_store = {schema["$id"]: schema for schema in schemas}

yaml = YAML()

def connector_validate(connector_dir, job_fail):
    for root, plugin_dirs, _ in os.walk(connector_dir):
        for plugin_dir in plugin_dirs:
            for _, _, files in os.walk(os.path.join(root, plugin_dir)):
                schema = json.load(open(f"schemas/{plugin_dir}.schema.json"))
                for file in files:
                    with open(os.path.join(root, plugin_dir, file), "r") as plugin_file:
                        plugin_data = yaml.load(plugin_file)

                    try:
                        resolver = RefResolver.from_schema(schema, store=schema_store)
                        validator = Draft7Validator(schema, resolver=resolver)
                        validator.validate(plugin_data)
                    except Exception as e:
                        job_fail = True
                        print(f"Validation error for {file} with message {str(e)}")

    return job_fail

job_fail = connector_validate("meltano/api/v1/", False)

if job_fail:
    print("Schema validation failed.")
    sys.exit(1)
else:
    print("All taps and targets pass the JSON Schema.")
    sys.exit()
