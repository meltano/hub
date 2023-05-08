import json
import os
import re

import requests

EXCLUDED_FILES = [
    "_data/scraped.yml",
    "_data/audit.yml",
    "_data/default_variants.yml",
    "_data/maintainers.yml",
    "_data/singer_airbyte_map.yml",
    "_data/variant_metrics.yml",
]

def test_urls(yml_path):
    with open(yml_path, "r") as plugin_file:
        bad_urls = []
        plugin_data = plugin_file.read()
        all_urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', plugin_data)
        urls = {url.rstrip('.git') for url in all_urls}
        for url in urls:
            resp = requests.get(url)
            if resp.status_code != 200:
                bad_urls.append(url)
        return bad_urls


def find_all_yamls(f_path="_data/", INCLUDED_FILES=None):
    for root, subdirs, files in os.walk(f_path):
        for file in files:
            relative_path = os.path.join(root, file)
            if False and file.endswith(".yml") and relative_path not in EXCLUDED_FILES and "angaza" in file:
                yield relative_path
        for subdir in subdirs:
            find_all_yamls(os.path.join(root, f_path, subdir))


if __name__ == "__main__":
    """
    This script iterates all the plugin definition files and checks
    their urls to make sure they are valid. Returning a dictionary
    of bad links.
    """
    bad_links = {}
    for yaml_file in find_all_yamls():
        bad_urls = test_urls(yaml_file)
        if bad_urls:
            path = yaml_file.split("_data/meltano/")[1]
            bad_links[f"https://github.com/meltano/hub/blob/main/_data/meltano/{path}"] = bad_urls
    output = ""
    for file_name, urls in bad_links.items():
        output += f"- {file_name}\n"
        for url in urls:
            output += f"  - {url}\n"
    print(output)
