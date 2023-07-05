import os
import subprocess
import sys
from collections import OrderedDict

from ruamel.yaml import YAML

yaml = YAML()
yaml.preserve_quotes = True
yaml.default_flow_style = False

def insert_newlines(string, every=160):
    # TODO: this is not working because editing strings causes them
    # to get wrapped in double quotes which looks ugly.
    return string
    # lines = []
    # for i in range(0, len(string), every):
    #     lines.append(string[i:i+every])
    # return '\n'.join(lines)


def process(v):
    output = None
    if isinstance(v, dict):
        output = fix_yaml_dict_format(v)
    elif isinstance(v, list):
        new_l = []
        for i in v:
            if isinstance(i, str):
                new_l.append(i)
            else:
                new_l.append(process(i))
        output = new_l
    elif isinstance(v, str):
        if len(v) > 160:
            v = insert_newlines(v, every=160)
        output = v
    else:
        output = v
    return output


def fix_yaml_dict_format(od):
    res = OrderedDict()
    for k, v in sorted(od.items()):
        res[k] = process(v)
    return dict(res)


def fix_yaml(yml_path):
    """
    Reads in the yaml file and attempts to fix it before
    overwriting the existing contents.
    """
    print(f"Fixing: {yml_path}")
    with open(yml_path, "r") as plugin_file:
        plugin_data = yaml.load(plugin_file)
    with open(yml_path, "w") as plugin_file:
        updated_dict = fix_yaml_dict_format(plugin_data)
        yaml.dump(updated_dict, plugin_file)


def run_yamllint(path):
    print(f"Linting: {path}")
    subprocess.run(f"yamllint {path} -c .yamllint.yaml".split(" "))


def find_all_yamls(f_path="_data/"):
    for root, subdirs, files in os.walk(f_path):
        for file in files:
            if file.endswith(".yml"):
                yield os.path.join(root, file)
        for subdir in subdirs:
            find_all_yamls(os.path.join(root, f_path, subdir))


if __name__ == "__main__":
    """
    This script iterates all the plugin definition files and fixes
    their formatting, then runs yamllint to validate the changes.
    You can optionally provide a file path to target only a single file,
    otherwise the default is to iterate all yml files in the `_data/` directory.
    """
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        fix_yaml(file_path)
        run_yamllint(file_path)
    else:
        for yaml_file in find_all_yamls():
            fix_yaml(yaml_file)
            run_yamllint(yaml_file)
