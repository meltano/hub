import os
import sys

from ruamel.yaml import YAML

yaml = YAML()
data_dir = "_data"
directory = f"{data_dir}/meltano/"


def read_yaml(path):
    with open(path, "r") as f:
        data = yaml.load(f)
    return data


def write_updated_maintainers(data):
    with open(f"{data_dir}/maintainers.yml", "w") as f:
        from collections import OrderedDict

        yaml.dump(dict(OrderedDict(sorted(data.items()))), f)


def build_maintainers():
    maintainers_set = set()
    missing = set()
    updated_maintainers = read_yaml(f"{data_dir}/maintainers.yml")

    for plugin_type in os.listdir(directory):
        for plugin_name in os.listdir(os.path.join(directory, plugin_type)):
            for variant_yml in os.listdir(
                os.path.join(directory, plugin_type, plugin_name)
            ):
                plugin_data = read_yaml(
                    os.path.join(directory, plugin_type, plugin_name, variant_yml)
                )
                maintainers_set.add(
                    plugin_data.get("variant")
                )  # different casings will return as distinct items
                if plugin_data.get("variant").lower() not in updated_maintainers:
                    missing.add(plugin_data.get("variant"))
                    updated_maintainers[plugin_data.get("variant").lower()] = {
                        "label": "TODO: ADD LABEL",
                        "url": "/".join(plugin_data.get("repo").split("/")[:-1]),
                    }

    return maintainers_set, updated_maintainers, missing


def remove_extras(updated_maintainers, extras):
    for key in extras:
        updated_maintainers.pop(key)


if __name__ == "__main__":
    """
    This script iterates all the plugin definition files and compiles a set
    of maintainers. Then it compares it to what exists in the maintainers.yml file.
    It overwrites the existing file with an updated dict with 'TODO's for name labels
    to accelerate updates. It also exits with code 1 if there are extra or missing
    maintainers so CICD can use it to validate.
    """
    maintainers_set, updated_maintainers, missing = build_maintainers()

    extras = updated_maintainers.keys() - maintainers_set

    remove_extras(updated_maintainers, extras)
    write_updated_maintainers(updated_maintainers)

    if extras or missing:
        print(f"Extra Maintainers: {extras}")
        print(f"Missing Maintainers: {missing}")
        misspellings = set([
            variant for variant in extras | missing if variant.lower() != variant
        ])
        if misspellings:
            print(f"Possible misspellings (check casing): {misspellings}")

        sys.exit(1)
    else:
        print("All maintainers are present.")
        sys.exit()
