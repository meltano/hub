import csv
from ruamel.yaml import YAML
import os
from pathlib import Path
import json
from collections import OrderedDict

yaml = YAML()
file_path = '/Users/pnadolny/Documents/Git/GitHub/meltano/hub/utility_scripts/hub_bot/export.csv'
hub_root = '/Users/pnadolny/Documents/Git/GitHub/meltano/hub'
default_path = f'{hub_root}/_data/default_variants.yml'
maintainers_path = f'{hub_root}/_data/maintainers.yml'

def write_yaml(path, content):
    with open(path, "w") as f:
        yaml.dump(content, f)

def read_yaml(path):
    with open(path, "r") as f:
        data = yaml.load(f)
    return data

def write_definition(plugin_name, plugin_variant, plugin_type, plugin_definition):
    dir_name = os.path.join(hub_root, '_data', 'meltano', plugin_type, plugin_name)
    Path(dir_name).mkdir(parents=True, exist_ok=True)
    plugin_definition = dict(reversed(plugin_definition.items()))
    if not Path(os.path.join(dir_name, f'{plugin_variant}.yml')).exists():
        write_yaml(
            os.path.join(dir_name, f'{plugin_variant}.yml'),
            plugin_definition
        )

def handle_default_variant(plugin_name, plugin_variant, plugin_type):
    defaults = read_yaml(default_path)
    plugin_type_defaults = defaults[plugin_type]
    if plugin_name not in plugin_type_defaults:
        plugin_type_defaults[plugin_name] = plugin_variant
        # plugin_type_defaults = dict(OrderedDict(sorted(plugin_type_defaults.items())))
        defaults[plugin_type] = plugin_type_defaults
        write_yaml(default_path, defaults)
    
def handle_maintainer(plugin_variant, repo_url):
    updated_maintainers = read_yaml(maintainers_path)
    if plugin_variant not in updated_maintainers:
        updated_maintainers[plugin_variant] = {
            "label": "TODO: ADD LABEL",
            "url": "/".join(repo_url.split("/")[:-1]),
        }
    updated_maintainers = dict(OrderedDict(sorted(updated_maintainers.items())))
    write_yaml(maintainers_path, updated_maintainers)

def get_plugin_type(plugin_name):
    if 'tap' in plugin_name and 'target' in plugin_name:
        raise Exception(f'Type Unknown: {plugin_name}')
    if 'tap' in plugin_name:
        return 'extractors'
    if 'target' in plugin_name:
        return 'loaders'

    
def iterate_file():
    with open(file_path, "r") as f:
        reader = csv.reader(f)
        for index, row in enumerate(reader):
            if index == 0:
                print(f"Skipping header {row}")
                continue
            repo_url = row[0]
            plugin_name = row[1]
            plugin_variant = row[2].lower()
            is_pull_request_open = row[3]
            is_issue_open = row[4]
            plugin_definition = json.loads(row[5])
            plugin_type = get_plugin_type(plugin_name)
            write_definition(plugin_name, plugin_variant, plugin_type, plugin_definition)
            handle_default_variant(plugin_name, plugin_variant, plugin_type)
            handle_maintainer(plugin_variant, repo_url)

if __name__ == "__main__":
    iterate_file()