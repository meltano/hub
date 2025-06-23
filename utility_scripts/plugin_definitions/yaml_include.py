import os

from ruamel.yaml import YAML

yaml = YAML()


def merge(a, b, path=None, update=True):
    "http://stackoverflow.com/questions/7204805/python-dictionaries-of-dictionaries-merge"
    "merges b into a"
    if path is None:
        path = []
    for key in b:
        if key in a:
            if isinstance(a[key], dict) and isinstance(b[key], dict):
                merge(a[key], b[key], path + [str(key)])
            elif a[key] == b[key]:
                pass  # same leaf value
            elif isinstance(a[key], list) and isinstance(b[key], list):
                if a[key] == "variants" and b[key] == "variants":
                    for idx, val in enumerate(b[key]):
                        b_name = b[key][idx].get("name")
                        for index, variant in enumerate(a[key]):
                            a_name = a[key][index].get("name")
                            if b_name == a_name:
                                try:
                                    a[key][idx] = merge(
                                        a[key][idx],
                                        b[key][idx],
                                        path + [str(key), str(idx)],
                                        update=update,
                                    )
                                except IndexError:
                                    a[key].append(b[key][idx])
                else:
                    for idx, val in enumerate(b[key]):
                        try:
                            a[key][idx] = merge(
                                a[key][idx],
                                b[key][idx],
                                path + [str(key), str(idx)],
                                update=update,
                            )
                        except IndexError:
                            a[key].append(b[key][idx])
            elif update:
                a[key] = b[key]
            elif not update:
                pass
            else:
                raise Exception("Conflict at %s" % ".".join(path + [str(key)]))
        else:
            a[key] = b[key]
    return a


with open("_data/scraped.yml", "r") as scraped_file:
    scraped = yaml.load(scraped_file)

directory = "_data/singer/"

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    print(f)
    plugin_name = filename.split(".")[0]

    with open(f, "r") as plugin_file:
        plugin_data = yaml.load(plugin_file)

    includes = plugin_data.get("include").split("/")
    include_source = includes[0]
    include_key = includes[1]
    if include_source == "scraped":
        merge_data = scraped.get(include_key)

        plugin_updated = merge(plugin_data, merge_data, update=False)

        with open(f"_data/taps/{plugin_name}.yml", "w") as outfile:
            yaml.dump(plugin_updated, outfile, default_flow_style=False)
