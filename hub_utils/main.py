import typer
from hub_utils.utilities import Utilities
from typing import Optional
from hub_utils.yaml_lint import find_all_yamls
import os

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
        if yaml_file == f'{util.hub_root}{starting_yaml}':
            start = True
        elif not start:
            print(f"Skipping SDK based: {yaml_file}")
            continue
        if "keywords" in data and "meltano_sdk" in data.get("keywords"):
            print(f"Updating: {yaml_file}")
            try:
                util.update_sdk(data.get('repo'), data.get("name"))
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
        if not starting_yaml or yaml_file == f'{util.hub_root}{starting_yaml}':
            start = True
        elif not start:
            print(f"Skipping SDK based: {yaml_file}")
            continue
        if "keywords" in data and "meltano_sdk" in data.get("keywords"):
            print(f"Updating: {yaml_file}")
            try:
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
                file_name = os.path.basename(yaml_file).replace('.yml', '.json')
                util._write_dict(
                    f"{output_dir}/{p_type}/{p_name}/{file_name}",
                    sdk_def
                )
            except Exception as e:
                failures.append(yaml_file)
                print(e)
    print(failures)