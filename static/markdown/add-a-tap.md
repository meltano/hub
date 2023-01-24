---
title: "Add a Tap or Target to Meltano Hub"
description: "Find out how to get your plugins on the MeltanoHub"
---

# Add a Plugin to the MeltanoHub

1. Clone the MeltanoHub Repo

```
git clone git@github.com:meltano/hub.git
```

2. Add or Update Plugin Definition

All Singer definitions are stored in `/_data/meltano/extractors/` or `/_data/meltano/loaders/` and logo images are in /assets/logos/<extractors or loaders>. Each variant of a plugin is stored under a directory named after the plugin (e.g.`/_data/meltano/extractors/tap-github/meltanolabs.yml`).

Use the following template to create your YAML file.

```yaml
capabilities:
  # Chose the capabilities that the connector supports
  # Checkout for a list and details - https://hub.meltano.com/singer/docs#singer-connector-capabilities
  # Tap Capability Options
  - about
  - activate-version
  - batch
  - stream-maps
  - schema-flattening
  - catalog
  - properties
  - discover
  - state
  - test
  - log-based
  # Target Capability Options
  - about
  - activate-version
  - batch
  - stream-maps
  - schema-flattening
  - soft-delete
  - hard-delete
  - datatype-failsafe
  - record-flattening
description: Code hosting platform # General description of what the company behind the API does
domain_url: URL of the developer documentation or website
keywords:
  # Attributes about the plugin for easier searching. Include `meltano_sdk` here if built using the SDK.
  # Other examples could be source type: `api`, `file`, `database`, etc. or cloud name `aws`, `gcp`, etc.
  - api
  - meltano_sdk
label: GitHub
logo_url: /assets/logos/extractors/github.png
maintenance_status: active # Options: active, beta, development, inactive, unknown
name: tap-github # The unique name of the connector
namespace: tap_github # The namespace e.g. tap_github
pip_url: git+<git_url>.git or pip install name
repo: https://github.com/MeltanoLabs/tap-github
settings:
- name: api_key
  label: API Key
  kind: password
  description: The API key for this source.
- name: start_date
  label: Start date
  description: Start date of when to start retrieve data from.
- name: my_other_setting
  label: My Other Setting
  description: Some other setting
settings_group_validation:
  # The set of required settings.
  - api_key
  - start_date
variant: meltanolabs # the github namespace
```

3. Add a Logo

Add or update the logo image in `/assets/logos/<extractors or loaders>`.

4. Add or Update default_variants.yml

If the plugin is new or if the default variant is changing then update the `/_data/default_variants.yml` file with the plugin name and its associated default variant name.

5. Add or Update maintainers.yml

The plugin variant name is usually the github namespaces that the plugin lives in.
If its not already listed in `/_data/maintainers.yml` then they should be added along with a link and label.

6. Lint Your Changes

Optionally run the yaml_lint_fix.py script over the files you updated to make them conform with the yamlint settings for this repo.

```
poetry install
poetry run python utility_scripts/plugin_definitions/yaml_lint_fix.py _data/meltano/extractors/tap-github/meltanolabs.yml
poetry run python utility_scripts/plugin_definitions/yaml_lint_fix.py _data/default_variants.yml
poetry run python utility_scripts/plugin_definitions/yaml_lint_fix.py _data/maintainers.yml
```

See the [CONTRIBUTING.md](https://github.com/meltano/hub/blob/main/CONTRIBUTING.md#linters) for more details.


7. Open a PR and Get Your PR Reviewed

[Open a pull request](https://github.com/meltano/hub/pulls) on the MeltanoHub repo and tag `@tayloramurphy` or `@pnadolny13` to flag it for review. You can optionally post to the [#hub](https://meltano.slack.com/archives/C01UGBSJNG5) channel on Meltano's [Slack](https://meltano.com/slack) workspace.
