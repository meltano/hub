import csv
import hashlib
import json
import os
from copy import copy
from datetime import datetime
from enum import Enum

import requests
import typer

from hub_utils.meltano_util import MeltanoUtil
from hub_utils.s3 import S3
from hub_utils.utilities import Utilities
from hub_utils.yaml_lint import find_all_yamls, fix_yaml, run_yamllint

app = typer.Typer()

SDK_SUFFIX_LIST = [
    "extractors/tap-circle-ci/meltanolabs",
    "extractors/tap-cloudwatch/meltanolabs",
    "extractors/tap-csv/meltanolabs",
    "extractors/tap-dbt/meltanolabs",
    "extractors/tap-duckdb/meltanolabs",
    "extractors/tap-github/meltanolabs",
    "extractors/tap-google-analytics/meltanolabs",
    "extractors/tap-jaffle-shop/meltanolabs",
    "extractors/tap-messagebird/meltanolabs",
    "extractors/tap-postgres/meltanolabs",
    "extractors/tap-slack/meltanolabs",
    "extractors/tap-snowflake/meltanolabs",
    "extractors/tap-stackexchange/meltanolabs",
    "loaders/target-csv/meltanolabs",
    "loaders/target-postgres/meltanolabs",
    "loaders/target-snowflake/meltanolabs",
    "loaders/target-yaml/meltanolabs",
]


@app.callback()
def callback():
    """
    [MeltanoHub](https://hub.meltano.com/) Utilities - A utility CLI intended
    to streamline the work needed to maintain MeltanoHub.

    **Installation**

    ```
    export HUB_ROOT_PATH='/Users/meltano/hub'

    poetry install
    poetry run hub-utils --help
    ```

    **Tests**

    ```bash
    poetry run pytest -v

    poetry run pytest -v tests/test_meltano_utils.py::test_sdk_about_parsing_1
    ```

    **Refreshing This README**

    The CLI is auto documenting so put all content in the CLI modules
    and this will use [typer-cli](https://typer.tiangolo.com/typer-cli/) utilities
    to render them as markdown.

    Run the following command:

    ```bash
    poetry run typer hub_utils/main.py utils docs --name hub-utils --output README.md
    ```

    """


class YamlLint(str, Enum):
    fix = "fix"
    lint = "lint"


@app.command()
def yamllint(action: YamlLint, paths: list[str] | None = None):
    """
    Run yamllint on all yamls in the hub or a specific path.
    """
    if not paths:
        paths = list(find_all_yamls())

    for path in paths:
        if action == YamlLint.lint:
            run_yamllint(path, error_if_fail=True)
        elif action == YamlLint.fix:
            fix_yaml(path)


@app.command()
def add(repo_url: str | None = None, auto_accept: bool = typer.Option(False)):
    """
    Add a new tap or target to the hub.
    It will prompt you for any attributes that need input.

    If the plugin is SDK based it will do its best to install the plugin and scrape
    the settings for you. It will prompt you for any missing attributes. If its not
    SDK based it will prompt you for settings 1 at a time and help you by suggesting
    defaults that you can accept or override.
    """
    util = Utilities(auto_accept)
    if not repo_url:
        repo_url = util._prompt("repo_url")
    if "airbytehq/airbyte" in repo_url:
        if util._prompt("Is this an Airbyte variant?", True, type=bool):
            util.add_airbyte(repo_url)
            return

    util.add(repo_url)
    if "hotglue" in repo_url:
        if util._prompt("Is this a Hotglue variant?", True, type=bool):
            # Attempt to scrape logo from hotglue's website
            name = repo_url.split("/")[-1]
            service_name = name.replace("tap-", "").replace("target-", "")
            ext = ".svg"
            url = (
                "https://s3.amazonaws.com/cdn.hotglue.xyz/"
                f"images/logos/{service_name}{ext}"
            )
            resp = requests.get(url)
            if resp.status_code != 200:
                ext = ".png"
                url = (
                    f"https://s3.amazonaws.com/cdn.hotglue.xyz/images/"
                    f"logos/{service_name}{ext}"
                )
                resp = requests.get(url)
                if resp.status_code != 200:
                    ext = ".jpeg"
                    url = (
                        "https://s3.amazonaws.com/cdn.hotglue.xyz/"
                        f"images/logos/{service_name}{ext}"
                    )
                    resp = requests.get(url)
                    if resp.status_code != 200:
                        ext = ".webp"
                        url = (
                            f"https://s3.amazonaws.com/cdn.hotglue.xyz/images"
                            f"/logos/{service_name}{ext}"
                        )
                        resp = requests.get(url)
                        if resp.status_code != 200:
                            print(f"Unable to find logo for {service_name}")
                            return
            with open(
                f"{util.hub_root}/static/assets/logos/extractors/{service_name}{ext}",
                "wb",
            ) as f:
                f.write(resp.content)


@app.command()
def update_definition(
    repo_url: str | None = None,
    plugin_name: str | None = None,
    auto_accept: bool = typer.Option(False),
):
    """
    Update the definition of a tap or target in the hub.

    Similar to the `add` command it will try to auto update using SDK settings or prompt
    you for input. When merging it will use the following rules:
    - if SDK setting description is empty it prefers the existing description
    - if the existing description longer than the scraped setting and has new lines
        then its likely manually overridden on the hub so prefer that one.
    """
    util = Utilities(auto_accept)
    if util._prompt("is_meltano_sdk", True, type=bool):
        util.update_sdk(repo_url, plugin_name)
    else:
        util.update(repo_url, plugin_name)


@app.command()
def update_quality(
    metrics_file_path: str,
):
    """
    Update the quality of all taps and targets on the hub.

    This command accepts a path to the [variant_metrics.yml]
    (https://github.com/meltano/hub/blob/main/_data/variant_metrics.yml)
    yaml file, make sure its the most up to date version likely sourced from S3.
    """
    util = Utilities(True)
    usage_metrics = util._read_yaml(metrics_file_path)["metrics"]
    for yaml_file in find_all_yamls(f_path=f"{util.hub_root}/_data/meltano/"):
        if yaml_file.split("/")[-3] not in ("extractors", "loaders"):
            continue
        data = util._read_yaml(yaml_file)
        is_sdk_based = False

        if "keywords" in data and "meltano_sdk" in data.get("keywords"):
            is_sdk_based = True
        usage_count = usage_metrics.get(data["repo"], {}).get("all_projects", 0)
        orig_quality = copy(data["quality"])
        # TODO: Calculate responsiveness
        responsiveness = "high"
        data["quality"] = MeltanoUtil.get_quality(
            data["variant"], is_sdk_based, usage_count, responsiveness
        )
        if orig_quality != data["quality"]:
            util._write_yaml(yaml_file, data, reformat=True)


@app.command()
def sdk_variants_as_csv():
    """
    Generate a `sdk.csv` CSV file in the current directory containing the following
    columns:
    plugin_type, name, variant, sdk
    """
    util = Utilities(True)
    base_repo_path = os.path.dirname(os.path.dirname(__file__))
    with open(f"{base_repo_path}/sdk.csv", "w") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["plugin_type", "name", "variant", "sdk"])

        for yaml_file in find_all_yamls(f_path=f"{util.hub_root}/_data/meltano/"):
            data = util._read_yaml(yaml_file)
            p_type, p_name, p_variant = yaml_file.split("/")[-3:]
            p_variant = p_variant.replace(".yml", "")
            sdk = False
            if "keywords" in data and "meltano_sdk" in data.get("keywords"):
                sdk = True
            csvwriter.writerow([p_type, p_name, p_variant, sdk])


@app.command()
def get_variant_names(
    hub_root: str,
    metadata_type: str = typer.Option("sdk"),
    # comma separated list
    plugin_type: str | None = None,
    skip: int = 0,
    limit: int = 10000,
):
    """
    NOTE: USED FOR
    [AUTOMATION](https://github.com/meltano/hub/tree/main/.github/workflows) ONLY

    Generate a list of variant names for a given set of filters.
    The list will be formatted as escaped JSON to be used by Github Actions.
    """
    util = Utilities(True)
    util.hub_root = hub_root
    formatted_output = util.get_variant_names(plugin_type, metadata_type, skip, limit)
    print(json.dumps(formatted_output).replace('"', '\\"'))


@app.command()
def extract_sdk_metadata_to_s3(
    variant_path_list: str,
    output_dir: str,
):
    """
    NOTE: USED FOR
    [AUTOMATION](https://github.com/meltano/hub/tree/main/.github/workflows) ONLY

    Extract the SDK metadata for the given variants and upload them to S3.
    """
    util = Utilities(True)
    for yaml_file in variant_path_list.split(","):
        data = util._read_yaml(yaml_file)
        p_type = util.get_plugin_type(data.get("repo"))
        p_name = data.get("name")
        sdk_def = util._test_exception(
            p_name,
            p_type,
            data.get("pip_url"),
            data.get("namespace"),
            data.get("executable", p_name),
            True,
        )
        hash_id = hashlib.md5(
            json.dumps(sdk_def, sort_keys=True, indent=2).encode("utf-8")
        ).hexdigest()
        file_path = os.path.basename(yaml_file).replace(".yml", "")
        file_name = file_path + ".json"
        local_file_path = f"{output_dir}/{p_type}/{p_name}/{hash_id}--{file_name}"
        util._write_dict(local_file_path, sdk_def)
        date_now = datetime.utcnow().strftime("%Y-%m-%d")
        s3_file_path = f"{p_type}/{p_name}/{file_path}/{hash_id}--{date_now}.json"
        s3_bucket = os.environ.get("AWS_S3_BUCKET")
        if not S3().hash_exists(s3_bucket, s3_file_path):
            print(f"Uploading: {s3_file_path}")
            S3().upload(s3_bucket, s3_file_path, local_file_path)
        else:
            print(f"Extract already exists: {s3_file_path}")


@app.command()
def upload_airbyte(
    variant_path_list: str,
    artifact_name: str,
):
    """
    NOTE: USED FOR
    [AUTOMATION](https://github.com/meltano/hub/tree/main/.github/workflows) ONLY

    Upload the given Airbyte artifacts to S3.
    """
    util = Utilities(True)
    yaml_file = variant_path_list
    for yaml_file in variant_path_list.split(","):
        spec_data = util._read_json(artifact_name)
        p_type, p_name, p_variant = yaml_file.split("/")[-3:]
        hash_id = hashlib.md5(
            json.dumps(spec_data, sort_keys=True, indent=2).encode("utf-8")
        ).hexdigest()
        file_path = os.path.basename(yaml_file).replace(".yml", "")
        date_now = datetime.utcnow().strftime("%Y-%m-%d")
        s3_file_path = f"{p_type}/{p_name}/{file_path}/{hash_id}--{date_now}.json"
        s3_bucket = os.environ.get("AWS_S3_BUCKET")
        if not S3().hash_exists(s3_bucket, s3_file_path):
            print(f"Uploading: {s3_file_path}")
            S3().upload(s3_bucket, s3_file_path, artifact_name)
        else:
            print(f"Extract already exists: {s3_file_path}")


# GITHUB ACTIONS
@app.command()
def download_metadata(
    local_path: str,
    variant_path_list: str | None = None,
    all_sdk: bool = True,
    ignore_list_str: str = "",
):
    """
    NOTE: USED FOR
    [AUTOMATION](https://github.com/meltano/hub/tree/main/.github/workflows) ONLY
    Download the latest metadata for the given variants from S3.
    """
    util = Utilities()
    s3 = S3()
    ignore_list = ignore_list_str.split(",")
    if not variant_path_list:
        variant_path_list = ",".join(SDK_SUFFIX_LIST)
    if all_sdk:
        variant_path_list = ",".join(
            [
                i["plugin-name"].split(".yml")[0]
                for i in util.get_variant_names(None, "sdk")
                if i["plugin-name"].split(".yml")[0] not in ignore_list
            ]
        )
    for yaml_file in variant_path_list.split(","):
        if not yaml_file:
            continue
        suffix = util.get_suffix(yaml_file)
        local_file_path = f"{local_path}/{suffix}.json"
        s3.download_latest(os.environ.get("AWS_S3_BUCKET"), suffix, local_file_path)


# GITHUB ACTIONS
@app.command()
def merge_metadata(
    hub_root: str,
    local_path: str,
    variant_path_list: str | None = None,
    all_sdk: bool = True,
):
    """
    NOTE: USED FOR
    [AUTOMATION](https://github.com/meltano/hub/tree/main/.github/workflows) ONLY

    Merge the latest SDK metadata from S3 with the existing hub
    """
    if not variant_path_list:
        variant_path_list = ",".join(
            [f"{hub_root}/_data/meltano/{suffix}.yml" for suffix in SDK_SUFFIX_LIST]
        )
    util = Utilities()
    util.hub_root = hub_root
    if all_sdk:
        variant_path_list = ",".join(
            [
                f"{hub_root}/_data/meltano/{i['plugin-name']}"
                for i in util.get_variant_names(None, "sdk")
            ]
        )
    for yaml_file in variant_path_list.split(","):
        suffix = util.get_suffix(yaml_file)
        local_file_path = f"{local_path}/{suffix}.json"
        if not os.path.exists(local_file_path):
            print(f"Skipping {suffix} as it does not exist locally")
            continue
        new_extract_json = util._read_json(local_file_path)
        existing_def = util._read_yaml(yaml_file)
        (
            new_settings,
            new_settings_group_validation,
            new_capabilities,
        ) = MeltanoUtil._parse_sdk_about_settings(new_extract_json)
        try:
            util.merge_and_update(
                existing_def,
                new_extract_json.get("name"),
                util.get_plugin_type_from_suffix(suffix),
                util.get_plugin_variant_from_suffix(suffix),
                new_settings,
                new_capabilities,
                new_settings_group_validation,
            )
        except Exception as e:
            print(f"Error merging {suffix}: {e}")
