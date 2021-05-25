import json
import os
import yaml
from copy import deepcopy

directory = '_data/taps/'
 
name_list = set()

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    plugin_name = filename.split(".")[0]

    with open(f, "r") as plugin_file:
        plugin_data = yaml.load(plugin_file)

    variants = plugin_data.get("variants")
    for variant in variants:
        name = variant.get("name")
        name_list.add(name)

print(name_list)

