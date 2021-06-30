import yaml
import json
import os
import sys

from jsonschema import validate


TAP_DIR = "_data/taps/"
TARGET_DIR = "_data/targets/"
SCHEMA_DIR = "singer/api/v1/schema.json"

job_fail = False

with open(SCHEMA_DIR, "r") as json_schema_file:
    schema = json.load(json_schema_file)

def connector_validate(connector_dir):
    for root, subdir, files in os.walk(connector_dir):

        for file in files:
            with open(os.path.join(root, file), "r") as plugin_file:
                plugin_data = yaml.load(plugin_file)
            
            try:
                validate(instance=plugin_data, schema=schema)
            except Exception as e:
                print(f"Validation error for {file} with message {str(e)}")
                job_fail = True

connector_validate(TAP_DIR)
connector_validate(TARGET_DIR)
if job_fail:
    sys.exit(1)
else:
    print("All taps and targest pass the JSON Schema.")
    sys.exit()

