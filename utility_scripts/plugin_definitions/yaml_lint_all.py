import os
import subprocess
from collections import OrderedDict

from ruamel.yaml import YAML

yaml = YAML()
yaml.preserve_quotes = True
yaml.default_flow_style = False

TAP_DIR = "_data/meltano/extractors/"
TARGET_DIR = "_data/meltano/loaders/"


def insert_newlines(string, every=160):
    # TODO: this is not working because editing strings causes them
    # to get wrapped in double quotes which looks ugly.
    return string
    # lines = []
    # for i in range(0, len(string), every):
    #     if string.startswith('"'):
    #         print('')
    #     lines.append(string[i:i+every])
    # return '\n'.join(lines)


def process(v):
    output = None
    if isinstance(v, dict):
        output = sort_ordered_dict(v)
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


def sort_ordered_dict(od):
    res = OrderedDict()
    if isinstance(od, str):
        print("")
    for k, v in sorted(od.items()):
        res[k] = process(v)
    return dict(res)


def _fix(yml_path):
    print(f"Fixing: {yml_path}")
    with open(yml_path, "r") as plugin_file:
        plugin_data = yaml.load(plugin_file)
    with open(yml_path, "w") as plugin_file:
        yaml.dump(sort_ordered_dict(plugin_data), plugin_file)


def lint(path):
    print(f"Linting: {path}")
    command = f"yamllint {path} -c .yamllint.yaml".split(" ")
    subprocess.run(command)


def find_all_yaml(f_path="_data/"):
    for root, subdirs, files in os.walk(f_path):
        for file in files:
            if file.endswith(".yml"):
                yield os.path.join(root, file)
        for subdir in subdirs:
            find_all_yaml(os.path.join(root, f_path, subdir))


if __name__ == "__main__":
    for yaml_file in find_all_yaml():
        print(yaml_file)
        _fix(yaml_file)
        lint(yaml_file)
