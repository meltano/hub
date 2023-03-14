# hub-utils

## Add

A utility CLI intended to streamline the steps needed to add Singer taps/targets to [MeltanoHub](https://hub.meltano.com/).

```
export HUB_ROOT_PATH='/Users/pnadolny/Documents/Git/GitHub/meltano/hub'

poetry install
poetry run hub_utils --help

poetry run hub_utils add https://github.com/MeltanoLabs/tap-google-analytics
poetry run hub_utils add https://github.com/MeltanoLabs/tap-google-analytics --auto-accept
```

## Bulk Add

This will iterate all reo_urls in a CSV file and prompt as it goes through.
After writing output it excludes the repo_url from an output CSV so you can pause iterating and restart. If skipped or added, it shouldnt prompt again.


```
poetry run hub_utils add-bulk /path/to/csv_file
```

## Add Airbyte

```
poetry run hub_utils add-airbyte
```

## Tests

```bash
poetry run pytest -v

poetry run pytest -v tests/test_core.py::test_sdk_about_parsing_1
```