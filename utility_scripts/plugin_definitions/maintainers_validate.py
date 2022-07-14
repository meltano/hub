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
    existing_maintainers = read_yaml(f"{data_dir}/maintainers.yml")

    for plugin_type in os.listdir(directory):
        for plugin_name in os.listdir(os.path.join(directory, plugin_type)):
            for variant_yml in os.listdir(
                os.path.join(directory, plugin_type, plugin_name)
            ):
                plugin_data = read_yaml(
                    os.path.join(directory, plugin_type, plugin_name, variant_yml)
                )
                maintainers_set.add(plugin_data.get("variant").lower())
                if plugin_data.get("variant").lower() not in existing_maintainers:
                    existing_maintainers[plugin_data.get("variant").lower()] = {
                        "label": "TODO: ADD LABEL",
                        "url": "/".join(plugin_data.get("repo").split("/")[:-1]),
                    }

    return maintainers_set, existing_maintainers


if __name__ == "__main__":
    """
        This script iterates all the plugin definition files and compiles a set
        of maintainers. Then it compares it to what exists in the maintainers.yml file.
        It overwrites the existing file with an updated dict with 'TODO's for name labels
        to accelerate updates. It also exits with code 1 if there are extra or missing
        maintainers so CICD can use it to validate.
    """
    maintainers_set, existing_maintainers = build_maintainers()

    extras = existing_maintainers.keys() - maintainers_set
    missing = maintainers_set - existing_maintainers.keys()

    write_updated_maintainers(existing_maintainers)

    if extras or missing:
        print(f"Extra Maintainers: {extras}")
        print(f"Missing Maintainers: {missing}")
        sys.exit(1)
    else:
        print("All maintainers are present.")
        sys.exit()
