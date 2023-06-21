import csv
import hashlib
import json
import os
from datetime import datetime

import requests
import typer

from hub_utils.meltano_util import MeltanoUtil
from hub_utils.s3 import S3
from hub_utils.utilities import Utilities
from hub_utils.yaml_lint import find_all_yamls

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
    MeltanoHub Utilities
    """


@app.command()
def add(repo_url: str = None, auto_accept: bool = typer.Option(False)):
    util = Utilities(auto_accept)
    util.add(repo_url)


@app.command()
def add_bulk(csv_path: str, auto_accept: bool = typer.Option(False)):
    util = Utilities(auto_accept)
    util.add_bulk(csv_path)


@app.command()
def update(repo_url: str = None, auto_accept: bool = typer.Option(False)):
    util = Utilities(auto_accept)
    util.update(repo_url)


@app.command()
def update_sdk(
    repo_url: str = None,
    plugin_name: str = None,
    auto_accept: bool = typer.Option(False),
):
    util = Utilities(auto_accept)
    util.update_sdk(repo_url, plugin_name)


@app.command()
def update_quality(
    metrics_file_path: str,
):
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
        # TODO: Calculate responsiveness
        responsiveness = "high"
        data["quality"] = MeltanoUtil.get_quality(
            data["variant"], is_sdk_based, usage_count, responsiveness
        )
        util._write_yaml(yaml_file, data)


@app.command()
def add_airbyte(repo_url: str = None, auto_accept: bool = typer.Option(False)):
    util = Utilities(auto_accept)
    util.add_airbyte(repo_url)


@app.command()
def add_hotglue(repo_url: str = None, auto_accept: bool = typer.Option(False)):
    util = Utilities(auto_accept)
    util.add(repo_url)
    name = repo_url.split("/")[-1]
    service_name = name.replace("tap-", "").replace("target-", "")
    ext = ".svg"
    url = f"https://s3.amazonaws.com/cdn.hotglue.xyz/images/logos/{service_name}{ext}"
    resp = requests.get(url)
    if resp.status_code != 200:
        ext = ".png"
        url = (
            f"https://s3.amazonaws.com/cdn.hotglue.xyz/images/logos/{service_name}{ext}"
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
        f"{util.hub_root}/static/assets/logos/extractors/{service_name}{ext}", "wb"
    ) as f:
        f.write(resp.content)


@app.command()
def sdk_variants_csv():
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
def refresh_sdk_variants(
    starting_yaml: str = None,
):
    util = Utilities(True)
    start = False
    failures = []
    for yaml_file in find_all_yamls(f_path=f"{util.hub_root}/_data/meltano/"):
        data = util._read_yaml(yaml_file)
        if yaml_file == f"{util.hub_root}{starting_yaml}":
            start = True
        elif not start:
            print(f"Skipping SDK based: {yaml_file}")
            continue
        if "keywords" in data and "meltano_sdk" in data.get("keywords"):
            print(f"Updating: {yaml_file}")
            try:
                util.update_sdk(data.get("repo"), data.get("name"))
            except Exception as e:
                failures.append(yaml_file)
                print(e)


@app.command()
def extract_metadata(
    output_dir: str,
    starting_yaml: str = None,
):
    util = Utilities(True)
    start = False
    failures = []
    for yaml_file in find_all_yamls(f_path=f"{util.hub_root}/_data/meltano/"):
        data = util._read_yaml(yaml_file)
        if not starting_yaml or yaml_file == f"{util.hub_root}{starting_yaml}":
            start = True
        elif not start:
            print(f"Skipping SDK based: {yaml_file}")
            continue
        if "keywords" in data and "meltano_sdk" in data.get("keywords"):
            print(f"Updating: {yaml_file}")
            p_type = util.get_plugin_type(data.get("repo"))
            p_name = data.get("name")
            sdk_def = util._test(
                p_name,
                p_type,
                data.get("pip_url"),
                data.get("namespace"),
                data.get("executable", p_name),
                True,
            )
            if not sdk_def:
                failures.append(yaml_file)
                continue
            file_name = os.path.basename(yaml_file).replace(".yml", ".json")
            util._write_dict(f"{output_dir}/{p_type}/{p_name}/{file_name}", sdk_def)
    print(failures)


@app.command()
def get_variant_names(
    hub_root: str,
    metadata_type: str = typer.Option("sdk"),
    # comma separated list
    plugin_type: str = None,
):
    formatted_output = []
    util = Utilities(True)
    for yaml_file in find_all_yamls(f_path=f"{hub_root}/_data/meltano/"):
        data = util._read_yaml(yaml_file)
        if plugin_type and yaml_file.split("/")[-3] not in plugin_type.split(","):
            continue

        if metadata_type == "sdk":
            if "meltano_sdk" not in data.get("keywords", []):
                continue
            suffix = "/".join(yaml_file.split("/")[-3:])
            formatted_output.append({"plugin-name": suffix})

        if metadata_type == "airbyte":
            if "airbyte_protocol" not in data.get("keywords", []):
                continue
            suffix = "/".join(yaml_file.split("/")[-3:])
            image_name = [
                setting.get("value")
                for setting in data.get("settings")
                if setting.get("name") == "airbyte_spec.image"
            ][0]
            if not image_name:
                continue
            formatted_output.append(
                {
                    "plugin-name": suffix,
                    "source-name": image_name.replace("airbyte/", ""),
                }
            )
    print(json.dumps(formatted_output).replace('"', '\\"'))


@app.command()
def extract_sdk_metadata_to_s3(
    variant_path_list: str,
    output_dir: str,
):
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


@app.command()
def translate_sdk(
    variant_path_list: str,
    sdk_output_path: str,
):
    util = Utilities(True)

    for yaml_file in variant_path_list.split(","):
        existing_def = util._read_yaml(yaml_file)
        p_type, p_name, p_variant = yaml_file.split("/")[-3:]
        p_variant = p_variant.replace(".yml", "")
        suffix = f"{p_type}/{p_name}/{p_variant}"
        local_file_path = f"{sdk_output_path}/{suffix}.json"
        S3().download_latest(os.environ.get("AWS_S3_BUCKET"), suffix, local_file_path)

        with open(local_file_path, "r") as f:
            sdk_about = json.load(f)
        (
            settings,
            settings_group_validation,
            capabilities,
        ) = MeltanoUtil._parse_sdk_about_settings(sdk_about)
        new_def = util._merge_definitions(
            existing_def,
            settings,
            util._string_to_literal(
                util._scrape_keywords(True, existing_def.get("keywords"))
            ),
            existing_def.get("maintenance_status"),
            capabilities,
            settings_group_validation,
        )
        util._write_updated_def(p_name, p_variant, p_type, new_def)
        util._reformat(p_type, p_name, p_variant)


# GITHUB ACTIONS
@app.command()
def download_metadata(
    local_path: str,
    variant_path_list: str = None,
):
    util = Utilities()
    s3 = S3()
    if not variant_path_list:
        variant_path_list = ",".join(SDK_SUFFIX_LIST)
    for yaml_file in variant_path_list.split(","):
        suffix = util.get_suffix(yaml_file)
        local_file_path = f"{local_path}/{suffix}.json"
        s3.download_latest(os.environ.get("AWS_S3_BUCKET"), suffix, local_file_path)


# GITHUB ACTIONS
@app.command()
def merge_metadata(
    hub_root: str,
    local_path: str,
    variant_path_list: str = None,
):
    if not variant_path_list:
        variant_path_list = ",".join(
            [f"{hub_root}/_data/meltano/{suffix}.yml" for suffix in SDK_SUFFIX_LIST]
        )
    util = Utilities()
    util.hub_root = hub_root
    for yaml_file in variant_path_list.split(","):
        suffix = util.get_suffix(yaml_file)
        local_file_path = f"{local_path}/{suffix}.json"
        new_extract_json = util._read_json(local_file_path)
        existing_def = util._read_yaml(yaml_file)
        (
            new_settings,
            new_settings_group_validation,
            new_capabilities,
        ) = MeltanoUtil._parse_sdk_about_settings(new_extract_json)
        util.merge_and_update(
            existing_def,
            new_extract_json.get("name"),
            util.get_plugin_type_from_suffix(suffix),
            util.get_plugin_variant_from_suffix(suffix),
            new_settings,
            new_capabilities,
            new_settings_group_validation,
        )
