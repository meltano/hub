# `hub-utils`

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

**Usage**:

```console
$ hub-utils [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `add`: Add a new tap or target to the hub.
* `download-metadata`: NOTE: USED FOR...
* `extract-sdk-metadata-to-s3`: NOTE: USED FOR...
* `get-variant-names`: NOTE: USED FOR...
* `merge-metadata`: NOTE: USED FOR...
* `sdk-variants-as-csv`: Generate a `sdk.csv` CSV file in the...
* `update-definition`: Update the definition of a tap or target...
* `update-quality`: Update the quality of all taps and targets...
* `upload-airbyte`: NOTE: USED FOR...
* `yamllint`: Run yamllint on all yamls in the hub or a...

## `hub-utils add`

Add a new tap or target to the hub.
It will prompt you for any attributes that need input.

If the plugin is SDK based it will do its best to install the plugin and scrape
the settings for you. It will prompt you for any missing attributes. If its not
SDK based it will prompt you for settings 1 at a time and help you by suggesting
defaults that you can accept or override.

**Usage**:

```console
$ hub-utils add [OPTIONS]
```

**Options**:

* `--repo-url TEXT`
* `--auto-accept / --no-auto-accept`: [default: no-auto-accept]
* `--help`: Show this message and exit.

## `hub-utils download-metadata`

NOTE: USED FOR
[AUTOMATION](https://github.com/meltano/hub/tree/main/.github/workflows) ONLY
Download the latest metadata for the given variants from S3.

**Usage**:

```console
$ hub-utils download-metadata [OPTIONS] LOCAL_PATH
```

**Arguments**:

* `LOCAL_PATH`: [required]

**Options**:

* `--variant-path-list TEXT`
* `--all-sdk / --no-all-sdk`: [default: no-all-sdk]
* `--help`: Show this message and exit.

## `hub-utils extract-sdk-metadata-to-s3`

NOTE: USED FOR
[AUTOMATION](https://github.com/meltano/hub/tree/main/.github/workflows) ONLY

Extract the SDK metadata for the given variants and upload them to S3.

**Usage**:

```console
$ hub-utils extract-sdk-metadata-to-s3 [OPTIONS] VARIANT_PATH_LIST OUTPUT_DIR
```

**Arguments**:

* `VARIANT_PATH_LIST`: [required]
* `OUTPUT_DIR`: [required]

**Options**:

* `--help`: Show this message and exit.

## `hub-utils get-variant-names`

NOTE: USED FOR
[AUTOMATION](https://github.com/meltano/hub/tree/main/.github/workflows) ONLY

Generate a list of variant names for a given set of filters.
The list will be formatted as escaped JSON to be used by Github Actions.

**Usage**:

```console
$ hub-utils get-variant-names [OPTIONS] HUB_ROOT
```

**Arguments**:

* `HUB_ROOT`: [required]

**Options**:

* `--metadata-type TEXT`: [default: sdk]
* `--plugin-type TEXT`
* `--help`: Show this message and exit.

## `hub-utils merge-metadata`

NOTE: USED FOR
[AUTOMATION](https://github.com/meltano/hub/tree/main/.github/workflows) ONLY

Merge the latest SDK metadata from S3 with the existing hub

**Usage**:

```console
$ hub-utils merge-metadata [OPTIONS] HUB_ROOT LOCAL_PATH
```

**Arguments**:

* `HUB_ROOT`: [required]
* `LOCAL_PATH`: [required]

**Options**:

* `--variant-path-list TEXT`
* `--help`: Show this message and exit.

## `hub-utils sdk-variants-as-csv`

Generate a `sdk.csv` CSV file in the current directory containing the following
columns:
plugin_type, name, variant, sdk

**Usage**:

```console
$ hub-utils sdk-variants-as-csv [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `hub-utils update-definition`

Update the definition of a tap or target in the hub.

Similar to the `add` command it will try to auto update using SDK settings or prompt
you for input. When merging it will use the following rules:
- if SDK setting description is empty it prefers the existing description
- if the existing description longer than the scraped setting and has new lines
    then its likely manually overridden on the hub so prefer that one.

**Usage**:

```console
$ hub-utils update-definition [OPTIONS]
```

**Options**:

* `--repo-url TEXT`
* `--plugin-name TEXT`
* `--auto-accept / --no-auto-accept`: [default: no-auto-accept]
* `--help`: Show this message and exit.

## `hub-utils update-quality`

Update the quality of all taps and targets on the hub.

This command accepts a path to the [variant_metrics.yml]
(https://github.com/meltano/hub/blob/main/_data/variant_metrics.yml)
yaml file, make sure its the most up to date version likely sourced from S3.

**Usage**:

```console
$ hub-utils update-quality [OPTIONS] METRICS_FILE_PATH
```

**Arguments**:

* `METRICS_FILE_PATH`: [required]

**Options**:

* `--help`: Show this message and exit.

## `hub-utils upload-airbyte`

NOTE: USED FOR
[AUTOMATION](https://github.com/meltano/hub/tree/main/.github/workflows) ONLY

Upload the given Airbyte artifacts to S3.

**Usage**:

```console
$ hub-utils upload-airbyte [OPTIONS] VARIANT_PATH_LIST ARTIFACT_NAME
```

**Arguments**:

* `VARIANT_PATH_LIST`: [required]
* `ARTIFACT_NAME`: [required]

**Options**:

* `--help`: Show this message and exit.

## `hub-utils yamllint`

Run yamllint on all yamls in the hub or a specific path.

**Usage**:

```console
$ hub-utils yamllint [OPTIONS] ACTION:{fix|lint} PATHS...
```

**Arguments**:

* `ACTION:{fix|lint}`: [required]
* `PATHS...`: [required]

**Options**:

* `--help`: Show this message and exit.
