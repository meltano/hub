import hashlib
import json
import os
from datetime import datetime
from typing import Optional

import typer

from hub_utils.meltano_util import MeltanoUtil
from hub_utils.s3 import S3
from hub_utils.utilities import Utilities
from hub_utils.yaml_lint import find_all_yamls

app = typer.Typer()

@app.callback()
def callback():
    """
    MeltanoHub Utilities
    """

@app.command()
def add(
    repo_url: str = None,
    auto_accept: bool = typer.Option(False)
):
    util = Utilities(auto_accept)
    util.add(repo_url)

@app.command()
def add_bulk(
    csv_path: str,
    auto_accept: bool = typer.Option(False)
):
    util = Utilities(auto_accept)
    util.add_bulk(csv_path)

@app.command()
def update(
    repo_url: str = None,
    auto_accept: bool = typer.Option(False)
):
    util = Utilities(auto_accept)
    util.update(repo_url)

@app.command()
def update_sdk(
    repo_url: str = None,
    plugin_name: str = None,
    auto_accept: bool = typer.Option(False)
):
    util = Utilities(auto_accept)
    util.update_sdk(repo_url, plugin_name)

@app.command()
def add_airbyte(
    repo_url: str = None,
    auto_accept: bool = typer.Option(False)
):
    util = Utilities(auto_accept)
    util.add_airbyte(repo_url)

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
                True
            )
            if not sdk_def:
                failures.append(yaml_file)
                continue
            file_name = os.path.basename(yaml_file).replace(".yml", ".json")
            util._write_dict(
                f"{output_dir}/{p_type}/{p_name}/{file_name}",
                sdk_def
            )
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
            formatted_output.append({"plugin-name":suffix})

        if metadata_type == "airbyte":
            if "airbyte_protocol" not in data.get("keywords", []):
                continue
            suffix = "/".join(yaml_file.split("/")[-3:])
            image_name = [setting.get("value") for setting in data.get("settings") if setting.get("name") == "airbyte_spec.image"][0]
            if not image_name:
                continue
            formatted_output.append({"plugin-name": suffix, "source-name": image_name.replace("airbyte/", "")})
    print(json.dumps(formatted_output).replace('\"', '\\"'))

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
            True
        )
        hash_id = hashlib.md5(json.dumps(sdk_def, sort_keys=True, indent=2).encode("utf-8")).hexdigest()
        file_path = os.path.basename(yaml_file).replace(".yml", "")
        file_name = file_path + ".json"
        local_file_path = f"{output_dir}/{p_type}/{p_name}/{hash_id}--{file_name}"
        util._write_dict(
            local_file_path,
            sdk_def
        )
        date_now = datetime.utcnow().strftime("%Y-%m-%d")
        s3_file_path = f"{p_type}/{p_name}/{file_path}/{hash_id}--{date_now}.json"
        s3_bucket = os.environ.get(
            "AWS_S3_BUCKET"
        )
        if not S3().hash_exists(s3_bucket, s3_file_path):
            print(f"Uploading: {s3_file_path}")
            S3().upload(
                s3_bucket,
                s3_file_path,
                local_file_path
            )
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
        hash_id = hashlib.md5(json.dumps(spec_data, sort_keys=True, indent=2).encode("utf-8")).hexdigest()
        file_path = os.path.basename(yaml_file).replace(".yml", "")
        date_now = datetime.utcnow().strftime("%Y-%m-%d")
        s3_file_path = f"{p_type}/{p_name}/{file_path}/{hash_id}--{date_now}.json"
        s3_bucket = os.environ.get(
            "AWS_S3_BUCKET"
        )
        if not S3().hash_exists(s3_bucket, s3_file_path):
            print(f"Uploading: {s3_file_path}")
            S3().upload(
                s3_bucket,
                s3_file_path,
                artifact_name
            )
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
        S3().download_latest(
            os.environ.get(
                "AWS_S3_BUCKET"
            ),
            suffix,
            local_file_path
        )

        with open(local_file_path, "r") as f:
            sdk_about = json.load(f)
        settings, settings_group_validation, capabilities = MeltanoUtil._parse_sdk_about_settings(sdk_about)
        new_def = util._merge_definitions(
            existing_def,
            settings,
            util._string_to_literal(util._scrape_keywords(True, existing_def.get("keywords"))),
            existing_def.get("maintenance_status"),
            capabilities,
            settings_group_validation,
        )
        util._write_updated_def(
            p_name,
            p_variant,
            p_type,
            new_def
        )
        util._reformat(p_type, p_name, p_variant)
