import json
import os
import sys
from pathlib import Path

from jsonschema import Draft7Validator, RefResolver
from ruamel.yaml import YAML

schemas = (json.load(open(source)) for source in Path(f"schemas").iterdir())
schema_store = {schema["$id"]: schema for schema in schemas}

yaml = YAML()

def is_plugin_valid(schema, plugin_dir, file_name):
    with open(os.path.join(file_path, plugin_dir, file_name), "r") as plugin_file:
        plugin_data = yaml.load(plugin_file)
        resolver = RefResolver.from_schema(schema, store=schema_store)
        validator = Draft7Validator(schema, resolver=resolver)
        try:
            validator.validate(plugin_data)
        except Exception as e:
            print(f"Validation error for {file_name} with message {str(e)}")
            return False
        return True

def is_plugins_index_valid(file_path):
    schema = json.load(open(f"schemas/plugins_index.schema.json"))
    with open(os.path.join(file_path, "index"), "r") as type_index:
        type_index_data = yaml.load(type_index)

    resolver = RefResolver.from_schema(schema, store=schema_store)
    validator = Draft7Validator(schema, resolver=resolver)
    try:
        validator.validate(type_index_data)
    except Exception as e:
        print(f"Validation error for {file_path}index with message {str(e)}")
        return False
    return True

def is_plugin_type_index_valid(file_path):
    schema = json.load(open(f"schemas/plugin_type_index.schema.json"))
    with open(os.path.join(file_path, "index"), "r") as type_index:
        type_index_data = yaml.load(type_index)
    validator = Draft7Validator(schema)
    # , resolver=resolver)
    try:
        validator.validate(type_index_data)
    except Exception as e:
        print(f"Validation error for {file_path}/index with message {str(e)}")
        return False
    return True

def plugins_validate(file_path):
    print("API schema validation started...")
    all_valid = True
    validation_results = {}
    for plugin_dir in os.listdir(file_path):
        if plugin_dir == "index":
            if not is_plugins_index_valid(file_path):
                all_valid = False
            continue
        print(f"Validating API schema for plugin type: {plugin_dir}")
        schema = json.load(open(f"schemas/{plugin_dir}.schema.json"))
        count = 0
        for file_name in os.listdir(os.path.join(file_path, plugin_dir)):
            if file_name == "index":
                if not is_plugin_type_index_valid(os.path.join(file_path, plugin_dir)):
                    all_valid = False
                continue
            if not is_plugin_valid(schema, plugin_dir, file_name):
                all_valid = False
                # dont increment count
                continue
            count += 1
        validation_results[plugin_dir] = count

    print("API schema validation complete.")
    if all_valid:
        print("All plugins pass the JSON Schema.")
        print(json.dumps(validation_results, indent=4, sort_keys=True))
        sys.exit()
    else:
        print("Schema validation failed.")
        print(validation_results)
        sys.exit(1)



file_path = "meltano/api/v1/plugins/"
# accept file path as optional argument
if len(sys.argv) > 1:
    file_path = sys.argv[1]

job_fail, validation_results = plugins_validate(file_path)


