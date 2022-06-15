import sys
from pprint import pprint

from deepdiff import DeepDiff
from deepdiff.helper import CannotCompare
from ruamel.yaml import YAML

yaml = YAML()

with open("meltano.yml", "r") as meltano_file:
    meltano = yaml.load(meltano_file)

with open("discovery.yml", "r") as hub_file:
    hub = yaml.load(hub_file)


def compare_func(x, y):
    try:
        return x["name"] == y["name"]
    except Exception:
        raise CannotCompare() from None


ddiff = DeepDiff(
    meltano,
    hub,
    verbose_level=2,
    get_deep_distance=True,
    cutoff_distance_for_pairs=1,
    cutoff_intersection_for_pairs=1,
    ignore_order=True,
    iterable_compare_func=compare_func,
)

if len(ddiff) == 0:
    print("Generated discovery.yml matches Meltano discovery.yml")
    sys.exit()
else:
    print("Generated discovery.yml does not match Meltano discovery.yml")
    pprint(ddiff, indent=2)
    sys.exit(1)
