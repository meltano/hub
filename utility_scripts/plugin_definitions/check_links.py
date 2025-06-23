import os

import requests
from ruamel.yaml import YAML

yaml = YAML()
yaml.preserve_quotes = True
yaml.default_flow_style = False

EXCLUDED_FILES = [
    "_data/scraped.yml",
    "_data/audit.yml",
    "_data/default_variants.yml",
    "_data/maintainers.yml",
    "_data/singer_airbyte_map.yml",
    "_data/variant_metrics.yml",
]

URL_KEYS = [
    "repo",
    "ext_repo",
]


def validate_urls(yml_path):
    with open(yml_path, "r") as plugin_file:
        bad_urls = []
        plugin_data = yaml.load(plugin_file)
        for key in URL_KEYS:
            url = plugin_data.get(key)
            if not url:
                continue
            try:
                resp = requests.get(url)
            except Exception:
                bad_urls.append(url)
                continue

            if resp.status_code != 200:
                bad_urls.append(url)
        return bad_urls


def find_all_yamls(f_path="_data/"):
    for root, subdirs, files in os.walk(f_path):
        for file in files:
            relative_path = os.path.join(root, file)
            if file.endswith(".yml") and relative_path not in EXCLUDED_FILES:
                yield relative_path
        for subdir in subdirs:
            find_all_yamls(os.path.join(root, f_path, subdir))


if __name__ == "__main__":
    """
    This script iterates all the plugin definition files and checks
    their urls to make sure they are valid. Returning bad links formatted
    as bullets and sub-bullets for populating the invalid_urls.md template.
    """
    bad_links = {}
    for yaml_file in find_all_yamls():
        bad_urls = validate_urls(yaml_file)
        if bad_urls:
            path = yaml_file.split("_data/meltano/")[1]
            bad_links[
                f"https://github.com/meltano/hub/blob/main/_data/meltano/{path}"
            ] = bad_urls
    output = ""
    for file_name, urls in bad_links.items():
        output += f"- {file_name}\n"
        for url in urls:
            output += f"  - {url}\n"
    print(output)
