import typer
from hub_utils.utilities import Utilities
from typing import Optional

app = typer.Typer()

@app.callback()
def callback():
    """
    MeltanoHub Utilities
    """

@app.command()
def add(
    repo_url: str,
    auto_accept: bool = typer.Option(False)
):
    util = Utilities(auto_accept)
    util.add(repo_url)
    # Utilities.scrape_sdk_metadata()
    # Utilities.scrape_sdk_metadata()
