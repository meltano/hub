import os

import requests
import yaml

MELTANO_DIR = "_data/meltano"
MELTANO_DISCOVERY_URL = "https://gitlab.com/meltano/meltano/-/raw/master/src/meltano/core/bundle/discovery.yml"


def get_discover_yaml():
    resp = requests.get(MELTANO_DISCOVERY_URL)
    data = resp.content
    return yaml.safe_load(data)


def get_file_name(plugin_name, plugin_type):
    if plugin_type == 'extractors':
        return plugin_name.split('tap-')[1]
    elif plugin_type == 'loaders':
        return plugin_name.split('target-')[1]
    else:
        return plugin_name

def write_file(plugin_def, file_path, file_name):
    os.makedirs(file_path, exist_ok=True)
    with open(f"{file_path}/{file_name}.yml", "w") as f:
        yaml.dump(plugin_def, f, sort_keys=False, default_flow_style=False)

def split_yaml(yaml_obj):
    for plugin_type in yaml_obj:
        plugins_list = yaml_obj.get(plugin_type)
        if isinstance(plugins_list, list):
            for plugin_def in plugins_list:
                file_name = get_file_name(plugin_def.get("name"), plugin_type)
                file_path = f"{MELTANO_DIR}/{plugin_type}"
                write_file(plugin_def, file_path, file_name)

if __name__ == "__main__":
    yml_obj = get_discover_yaml()
    split_yaml(yml_obj)
