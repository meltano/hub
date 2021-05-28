"""Script to create a metrics yaml file from an input file.

In the future, we plan to refactor this script into:
(1) - Map-transformer, which nests the result into the correct shape
(2) - Target-yaml, which serializes the output as a yaml file.

Instructions:

1. In athena SQL console, create a new worksheet and run:
   `select * from dbt.fact_repo_metrics`.
2. Download the CSV output and save to the CSV_INFILE path below.
3. cd into the `meltano` directory and run this script:
   `python3 scripts/create_metrics_yaml.py`
"""

import csv
from typing import Iterable
import yaml
from pathlib import Path

# Relative paths to meltano project folder:
CSV_INFILE = "data/fact_repo_metrics-20210528.csv"
YAML_OUTFILE = "../_data/metrics.yml"

# Which keys to save in metrics yaml output:
INCLUDE_KEYS = {
    "is_fork",
    "num_forks",
    "num_open_issues",
    "num_watchers",
    "num_stargazers",
    "created_at_timestamp",
    "last_push_timestamp",
    "last_updated_timestamp",
}


def read_records(source_file) -> Iterable[dict]:
    with open(source_file, newline="") as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=",", quotechar='"')
        for row in csvreader:
            yield row


def yaml_write(records, yaml_filepath):
    content_dict: dict = {}
    for record in records:
        repo_metrics = {}
        for key in INCLUDE_KEYS:
            repo_metrics[key] = yaml.safe_load(record[key])
        content_dict[record["repo_full_name"]] = repo_metrics
    Path(yaml_filepath).write_text(yaml.dump(content_dict))


if __name__ == "__main__":
    yaml_write(read_records(CSV_INFILE), YAML_OUTFILE)
