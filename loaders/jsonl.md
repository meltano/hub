---
title: JSON Lines (JSONL)
layout: plugin_page
description: Use Meltano to pull data from various sources and load it into JSON Lines (JSONL) files
---

The `target-jsonl` [loader](https://meltano.com/plugins/loaders/) loads [extracted](https://meltano.com/plugins/extractors/) data into [JSON Lines (JSONL)](https://jsonlines.org/) files.

- **Repository**: <https://github.com/andyh1203/target-jsonl>
- **Maintainer**: [Andy Huynh](https://github.com/andyh1203)
- **Maintenance status**: Active

## Getting Started

### Prerequisites

If you haven't already, follow the initial steps of the [Getting Started guide](https://docs.meltano.com/getting-started.html):

1. [Install Meltano](https://docs.meltano.com/getting-started.html#install-meltano)
1. [Create your Meltano project](https://docs.meltano.com/getting-started.html#create-your-meltano-project)
1. [Add an extractor to pull data from a source](https://docs.meltano.com/getting-started.html#add-an-extractor-to-pull-data-from-a-source)

### Installation and configuration

#### Using the Command Line Interface

1. Add the `target-jsonl` loader to your project using [`meltano add`](https://docs.meltano.com/command-line-interface.html#add):

    ```bash
    meltano add loader target-jsonl
    ```

1. Configure the [settings](#settings) below using [`meltano config`](https://docs.meltano.com/command-line-interface.html#config).

#### Using Meltano UI

1. Start [Meltano UI](https://docs.meltano.com/ui.html) using [`meltano ui`](https://docs.meltano.com/command-line-interface.html#ui):

    ```bash
    meltano ui
    ```

1. Open the Loaders interface at <http://localhost:5000/loaders>.
1. Click the "Add to project" button for "JSON Lines (JSONL)".
1. Configure the [settings](#settings) below in the "Configuration" interface that opens automatically.

### Next steps

Follow the remaining step of the [Getting Started guide](https://docs.meltano.com/getting-started.html):

1. [Run a data integration (EL) pipeline](https://docs.meltano.com/getting-started.html#run-a-data-integration-el-pipeline)

If you run into any issues, [learn how to get help](https://docs.meltano.com/getting-help.html).

## Settings

`target-jsonl` requires the [configuration](https://docs.meltano.com/configuration.html) of the following settings:

- [Destination Path](#destination-path)

These and other supported settings are documented below.
To quickly find the setting you're looking for, use the Table of Contents in the sidebar.

#### Minimal configuration

A minimal configuration of `target-jsonl` in your [`meltano.yml` project file](https://docs.meltano.com/project.html#meltano-yml-project-file) will look like this:

```yml{5-6}
plugins:
  loaders:
  - name: target-jsonl
    variant: andyh1203
    config:
      destination_path: my_jsonl_files
```

### Destination Path

- Name: `destination_path`
- [Environment variable](https://docs.meltano.com/configuration.html#configuring-settings): `TARGET_JSONL_DESTINATION_PATH`
- Default: `output`

Sets the destination path the JSONL files are written to, relative to the project root.

The directory needs to exist already, it will not be created automatically.

To write JSONL files to the project root, set an empty string (`""`).

#### How to use

Manage this setting using [Meltano UI](#using-meltano-ui), [`meltano config`](https://docs.meltano.com/command-line-interface.html#config), or an [environment variable](https://docs.meltano.com/configuration.html#configuring-settings):

```bash
meltano config target-jsonl set destination_path <path>

export TARGET_JSONL_DESTINATION_PATH=<path>
```

### Do Timestamp File

- Name: `do_timestamp_file`
- [Environment variable](https://docs.meltano.com/configuration.html#configuring-settings): `TARGET_JSONL_DO_TIMESTAMP_FILE`
- Default: `false`

Specifies if the files should get timestamped.

By default, the resulting file will not have a timestamp in the file name (i.e. `exchange_rate.jsonl`).

If this option gets set to `true`, the resulting file will have a timestamp associated with it (i.e. `exchange_rate-{timestamp}.jsonl`).

#### How to use

Manage this setting using [Meltano UI](#using-meltano-ui), [`meltano config`](https://docs.meltano.com/command-line-interface.html#config), or an [environment variable](https://docs.meltano.com/configuration.html#configuring-settings):

```bash
meltano config target-jsonl set do_timestamp_file true

export TARGET_JSONL_DO_TIMESTAMP_FILE=true
```
