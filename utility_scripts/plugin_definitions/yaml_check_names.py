import os
import sys

from ruamel.yaml import YAML

yaml = YAML()

TAP_DIR = "_data/meltano/extractors/"
TARGET_DIR = "_data/meltano/loaders/"

job_fail = False


def connector_validate(connector_dir):
    _success = True
    for root, subdir, files in os.walk(connector_dir):
        for file in files:
            with open(os.path.join(root, file), "r") as plugin_file:
                plugin_data = yaml.load(plugin_file)
                if plugin_data["name"] != root.rpartition("/")[-1]:
                    print(
                        f"Connector name {plugin_data['name']} does not match directory name {root.rpartition('/')[-1]} in {root}/{file}"
                    )
                    _success = False

    return _success


job_1 = connector_validate(TAP_DIR)
job_2 = connector_validate(TARGET_DIR)

if job_1 and job_2:
    print("All taps and targets have expected names.")
    sys.exit()
else:
    print("Schema validation failed.")
    sys.exit(1)
