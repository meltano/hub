---
title: BigQuery
layout: plugin_page
description: Use Meltano to pull data from various sources and load it into BigQuery
---

The `target-bigquery` [loader](https://meltano.com/plugins/loaders/) loads [extracted](https://meltano.com/plugins/extractors/) data into a [BigQuery](https://cloud.google.com/bigquery) data warehouse.

- **Repository**: <https://github.com/adswerve/target-bigquery>
- **Maintainer**: [Adswerve](https://adswerve.com/)
- **Maintenance status**: Active

## Getting Started

### Prerequisites

If you haven't already, follow the initial steps of the [Getting Started guide](https://docs.meltano.com/getting-started.html):

1. [Install Meltano](https://docs.meltano.com/getting-started.html#install-meltano)
1. [Create your Meltano project](https://docs.meltano.com/getting-started.html#create-your-meltano-project)
1. [Add an extractor to pull data from a source](https://docs.meltano.com/getting-started.html#add-an-extractor-to-pull-data-from-a-source)

Then, follow the steps in the ["Activate the Google BigQuery API" section of the repository's README](https://github.com/adswerve/target-bigquery#step-1-activate-the-google-bigquery-api).

### Installation and configuration

#### Using the Command Line Interface

1. Add the `target-bigquery` loader to your project using [`meltano add`](https://docs.meltano.com/command-line-interface.html#add):

    ```bash
    meltano add loader target-bigquery
    ```

1. Configure the [settings](#settings) below using [`meltano config`](https://docs.meltano.com/command-line-interface.html#config).

#### Using Meltano UI

1. Start [Meltano UI](https://docs.meltano.com/ui.html) using [`meltano ui`](https://docs.meltano.com/command-line-interface.html#ui):

    ```bash
    meltano ui
    ```

1. Open the Loaders interface at <http://localhost:5000/loaders>.
1. Click the "Add to project" button for "BigQuery".
1. Configure the [settings](#settings) below in the "Configuration" interface that opens automatically.

### Next steps

Follow the remaining step of the [Getting Started guide](https://docs.meltano.com/getting-started.html):

1. [Run a data integration (EL) pipeline](https://docs.meltano.com/getting-started.html#run-a-data-integration-el-pipeline)

If you run into any issues, chat with us in [#troubleshooting](https://meltano.slack.com/archives/C01TCRBBJD7) on [Slack](https://meltano.com/slack).

## Settings

`target-bigquery` requires the [configuration](https://docs.meltano.com/configuration.html) of the following settings:

- [Project ID](#project-id)
- [Dataset ID](#dataset-id)
- [Location](#location)
- [Credentials Path](#credentials-path)

These and other supported settings are documented below.
To quickly find the setting you're looking for, use the Table of Contents in the sidebar.

#### Minimal configuration

A minimal configuration of `target-bigquery` in your [`meltano.yml` project file](https://docs.meltano.com/concepts/project#meltano-yml-project-file) will look like this:

```yml{5-8}
plugins:
  loaders:
  - name: target-bigquery
    variant: adswerve
    config:
      project_id: my-project-id
      # dataset_id: my-dataset-id   # override if default (see below) is not appropriate
      location: EU
```

### Project ID

- Name: `project_id`
- [Environment variable](https://docs.meltano.com/configuration.html#configuring-settings): `TARGET_BIGQUERY_PROJECT_ID`

BigQuery project

#### How to use

Manage this setting using [Meltano UI](#using-meltano-ui), [`meltano config`](https://docs.meltano.com/command-line-interface.html#config), or an [environment variable](https://docs.meltano.com/configuration.html#configuring-settings):

```bash
meltano config target-bigquery set project_id <id>

export TARGET_BIGQUERY_PROJECT_ID=<id>
```

### Dataset ID

- Name: `dataset_id`
- [Environment variable](https://docs.meltano.com/configuration.html#configuring-settings): `TARGET_BIGQUERY_DATASET_ID`
- Default: `$MELTANO_EXTRACT__LOAD_SCHEMA`, which [will expand to](https://docs.meltano.com/configuration.html#expansion-in-setting-values) the value of the [`load_schema` extra](https://docs.meltano.com/concepts/plugins#load-schema-extra) for the extractor used in the pipeline, which defaults to the extractor's namespace, e.g. `tap_gitlab` for [`tap-gitlab`](https://meltano.com/plugins/extractors/gitlab.html).

BigQuery dataset

#### How to use

Manage this setting using [Meltano UI](#using-meltano-ui), [`meltano config`](https://docs.meltano.com/command-line-interface.html#config), or an [environment variable](https://docs.meltano.com/configuration.html#configuring-settings):

```bash
meltano config target-bigquery set dataset_id <id>

export TARGET_BIGQUERY_DATASET_ID=<id>
```

### Location

- Name: `location`
- [Environment variable](https://docs.meltano.com/configuration.html#configuring-settings): `TARGET_BIGQUERY_LOCATION`
- Default: `US`

Dataset location

See <https://cloud.google.com/bigquery/docs/locations>.

#### How to use

Manage this setting using [Meltano UI](#using-meltano-ui), [`meltano config`](https://docs.meltano.com/command-line-interface.html#config), or an [environment variable](https://docs.meltano.com/configuration.html#configuring-settings):

```bash
meltano config target-bigquery set location EU

export TARGET_BIGQUERY_LOCATION=EU
```

### Credentials Path

- Name: `credentials_path`
- [Environment variable](https://docs.meltano.com/configuration.html#configuring-settings): `TARGET_BIGQUERY_CREDENTIALS_PATH`, alias: `GOOGLE_APPLICATION_CREDENTIALS`
- Default: `$MELTANO_PROJECT_ROOT/client_secrets.json`

Fully qualified path to `client_secrets.json` for your service account.

See the ["Activate the Google BigQuery API" section of the repository's README](https://github.com/adswerve/target-bigquery#step-1-activate-the-google-bigquery-api) and <https://cloud.google.com/docs/authentication/production>.

By default, this file is expected to be at the root of your project directory.

#### How to use

Manage this setting using [Meltano UI](#using-meltano-ui), [`meltano config`](https://docs.meltano.com/command-line-interface.html#config), or an [environment variable](https://docs.meltano.com/configuration.html#configuring-settings):

```bash
meltano config target-bigquery set credentials_path /home/user/Downloads/client_secrets.json

export TARGET_BIGQUERY_CREDENTIALS_PATH=/home/user/Downloads/client_secrets.json
```

### Validate Records

- Name: `validate_records`
- [Environment variable](https://docs.meltano.com/configuration.html#configuring-settings): `TARGET_BIGQUERY_VALIDATE_RECORDS`
- Default: `false`

Validate records

#### How to use

Manage this setting using [Meltano UI](#using-meltano-ui), [`meltano config`](https://docs.meltano.com/command-line-interface.html#config), or an [environment variable](https://docs.meltano.com/configuration.html#configuring-settings):

```bash
meltano config target-bigquery set validate_records true

export TARGET_BIGQUERY_VALIDATE_RECORDS=true
```

### Add Metadata Columns

- Name: `add_metadata_columns`
- [Environment variable](https://docs.meltano.com/configuration.html#configuring-settings): `TARGET_BIGQUERY_ADD_METADATA_COLUMNS`
- Default: `false`

Add `_time_extracted` and `_time_loaded` metadata columns

#### How to use

Manage this setting using [Meltano UI](#using-meltano-ui), [`meltano config`](https://docs.meltano.com/command-line-interface.html#config), or an [environment variable](https://docs.meltano.com/configuration.html#configuring-settings):

```bash
meltano config target-bigquery set add_metadata_columns true

export TARGET_BIGQUERY_ADD_METADATA_COLUMNS=true
```

### Replication Method

- Name: `replication_method`
- [Environment variable](https://docs.meltano.com/configuration.html#configuring-settings): `TARGET_BIGQUERY_REPLICATION_METHOD`
- Options: `append`, `truncate`
- Default: `append`

Replication method, `append` or `truncate`

#### How to use

Manage this setting using [Meltano UI](#using-meltano-ui), [`meltano config`](https://docs.meltano.com/command-line-interface.html#config), or an [environment variable](https://docs.meltano.com/configuration.html#configuring-settings):

```bash
meltano config target-bigquery set replication_method truncate

export TARGET_BIGQUERY_REPLICATION_METHOD=truncate
```

### Table Prefix

- Name: `table_prefix`
- [Environment variable](https://docs.meltano.com/configuration.html#configuring-settings): `TARGET_BIGQUERY_TABLE_PREFIX`

Add prefix to table name

#### How to use

Manage this setting using [Meltano UI](#using-meltano-ui), [`meltano config`](https://docs.meltano.com/command-line-interface.html#config), or an [environment variable](https://docs.meltano.com/configuration.html#configuring-settings):

```bash
meltano config target-bigquery set table_prefix <prefix>

export TARGET_BIGQUERY_TABLE_PREFIX=<prefix>
```

### Table Suffix

- Name: `table_suffix`
- [Environment variable](https://docs.meltano.com/configuration.html#configuring-settings): `TARGET_BIGQUERY_TABLE_SUFFIX`

Add suffix to table name

#### How to use

Manage this setting using [Meltano UI](#using-meltano-ui), [`meltano config`](https://docs.meltano.com/command-line-interface.html#config), or an [environment variable](https://docs.meltano.com/configuration.html#configuring-settings):

```bash
meltano config target-bigquery set table_suffix <suffix>

export TARGET_BIGQUERY_TABLE_SUFFIX=<suffix>
```

### Max Cache

- Name: `max_cache`
- [Environment variable](https://docs.meltano.com/configuration.html#configuring-settings): `TARGET_BIGQUERY_MAX_CACHE`
- Default: `50`

Maximum cache size in MB

#### How to use

Manage this setting using [Meltano UI](#using-meltano-ui), [`meltano config`](https://docs.meltano.com/command-line-interface.html#config), or an [environment variable](https://docs.meltano.com/configuration.html#configuring-settings):

```bash
meltano config target-bigquery set max_cache 100

export TARGET_BIGQUERY_MAX_CACHE=100
```

### Table Config

- Name: `table_config`
- [Environment variable](https://docs.meltano.com/configuration.html#configuring-settings): `TARGET_BIGQUERY_TABLE_CONFIG`

A path to a file containing the definition of partitioning and clustering.

#### How to use

Manage this setting using [Meltano UI](#using-meltano-ui), [`meltano config`](https://docs.meltano.com/command-line-interface.html#config), or an [environment variable](https://docs.meltano.com/configuration.html#configuring-settings):

```bash
meltano config target-bigquery set table_config table_config.json

export TARGET_BIGQUERY_TABLE_CONFIG=table_config.json
```

### Merge State Messages

- Name: `merge_state_messages`
- [Environment variable](https://docs.meltano.com/configuration.html#configuring-settings): `TARGET_BIGQUERY_MERGE_STATE_MESSAGES`
- Default: `false`

Whether to merge multiple state messages from the tap into the state file or uses the last state message as the state file. Note that it is not recommended to set this to `true` when using with Meltano as the merge behavior conflicts with Meltano's merge process.

#### How to use

Manage this setting using [Meltano UI](#using-meltano-ui), [`meltano config`](https://docs.meltano.com/command-line-interface.html#config), or an [environment variable](https://docs.meltano.com/configuration.html#configuring-settings):

```bash
meltano config target-bigquery set merge_state_messages true

export TARGET_BIGQUERY_MERGE_STATE_MESSAGES=true
```
