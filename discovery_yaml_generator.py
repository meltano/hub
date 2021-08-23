import os
import re
from ruamel.yaml import yaml

DISCOVERY_VERSION = 18
MELTANO_DIR = "_data/meltano/"
DISCOVERY_FILE = "discovery.yml"

discovery_dict = {}
discovery_dict["version"] = DISCOVERY_VERSION

for root, subdir, files in os.walk(MELTANO_DIR):
    meltano_type = re.sub(MELTANO_DIR, "", root)
    if meltano_type == "":
        continue
    meltano_array = []

    for file in files:
        with open(os.path.join(root, file), "r") as plugin_file:
            plugin_data = yaml.load(plugin_file, Loader=yaml.FullLoader)

        meltano_array.append(plugin_data)

    discovery_dict[meltano_type] = meltano_array

with open(DISCOVERY_FILE, "a") as outfile:
    yaml.dump(discovery_dict, outfile)
