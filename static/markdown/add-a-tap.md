---
title: "Add a Tap or Target to Meltano Hub"
description: "Find out how to get your plugins on the MeltanoHub"
---

# Add a Tap to the MeltanoHub

1. Clone the MeltanoHub Repo & Create YAML File

```
git clone git@github.com:meltano/hub.git
```

All Singer definitions are stored in `/_data/meltano/extractors/` or `/_data/meltano/loaders/` and logo images are in /assets/logos/<extractors or loaders>. Add/update the file in the appropriate folder (`/taps` or `/targets`). The name of the file should match the name of the tap. If there is already one, add a descriptor to the name such as `-search`.

Use the following template to create your YAML file.

```yaml
description: General description of what the company behind the API does
label: Properly formatted label of the connector e.g. GitLab
name: The unique name of the connector
logo_url: /assets/logos/extractors/gitlab.png
namespace: The namespace e.g. tap_gitlab
variant: Name of the GitHub/GitLab namespace
pip_url: git+<git_url>.git or pip install name
repo: repo URL
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
settings_group_validation:
  # The set of required settings.
  - api_key
  - start_date
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
domain_url: URL of the developer documentation or website
maintenance_status: "Options: active, beta, development, inactive, unknown"
keywords:
  # Attributes about the plugin for easier searching. Include `meltano_sdk` here if built using the SDK.
  # Other examples could be source type: `api`, `file`, `database`, etc. or cloud name `aws`, `gcp`, etc.
  - api
  - meltano_sdk
```

1. Add a Logo

Add/update the PNG logo image in `/assets/logos/<taps or targets>`. The image name must match the YAML file name.

1. Open a PR and Get your PR Reviewed

[Open a pull request](https://github.com/meltano/hub/pulls) on the MeltanoHub repo and tag `@tayloramurphy` or `@pnadolny13` to flag it for review. You can optionally post to the [#hub](https://meltano.slack.com/archives/C01UGBSJNG5) channel on Meltano's [Slack](https://meltano.com/slack) workspace.
