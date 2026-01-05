"""Extract URLs from plugin YAML files for validation with lychee."""
import json
import os

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


def extract_urls_from_file(yml_path):
    """Extract URLs from a YAML file."""
    with open(yml_path) as plugin_file:
        plugin_data = yaml.load(plugin_file)
        urls = []
        for key in URL_KEYS:
            url = plugin_data.get(key)
            if url:
                urls.append(url)
        return urls


def find_all_yamls(f_path="_data/"):
    """Find all YAML files to process."""
    for root, subdirs, files in os.walk(f_path):
        for file in files:
            relative_path = os.path.join(root, file)
            if file.endswith(".yml") and relative_path not in EXCLUDED_FILES:
                yield relative_path
        for subdir in subdirs:
            find_all_yamls(os.path.join(root, f_path, subdir))


if __name__ == "__main__":
    """Extract all URLs and their source files, output as JSON for lychee."""
    url_to_files = {}

    for yaml_file in find_all_yamls():
        urls = extract_urls_from_file(yaml_file)
        for url in urls:
            if url not in url_to_files:
                url_to_files[url] = []
            path = yaml_file.split("_data/meltano/")[1] if "_data/meltano/" in yaml_file else yaml_file
            url_to_files[url].append(
                f"https://github.com/meltano/hub/blob/main/_data/meltano/{path}"
            )

    # Output URLs for lychee (one per line)
    for url in url_to_files:
        print(url)

    # Save mapping to file for later processing
    with open(".url_mapping.json", "w") as f:
        json.dump(url_to_files, f, indent=2)
