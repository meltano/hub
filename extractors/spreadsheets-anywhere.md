---
title: Spreadsheets Anywhere
layout: plugin_page
description: Use Meltano to pull data from CSV files and Excel spreadsheets on cloud or local storage and load it into Snowflake, PostgreSQL, and more
---


The `tap-spreadsheets-anywhere` [extractor](https://meltano.com/plugins/extractors/) pulls data from [CSV](https://en.wikipedia.org/wiki/Comma-separated_values) files and Excel spreadsheets on cloud or local storage.

- **Repository**: <https://github.com/ets/tap-spreadsheets-anywhere>
- **Maintainer**: [Eric Simmerman](https://github.com/ets)
- **Maintenance status**: Active

## Getting Started

### Prerequisites

If you haven't already, follow the initial steps of the [Getting Started guide](https://docs.meltano.com/getting-started.html):

1. [Install Meltano](https://docs.meltano.com/getting-started.html#install-meltano)
1. [Create your Meltano project](https://docs.meltano.com/getting-started.html#create-your-meltano-project)

### Installation and configuration

1. Add the `tap-spreadsheets-anywhere` extractor to your project using [`meltano add`](https://docs.meltano.com/command-line-interface.html#add):

    ```bash
    meltano add extractor tap-spreadsheets-anywhere
    ```

1. Configure the [settings](#settings) below using [`meltano config`](https://docs.meltano.com/command-line-interface.html#config).

### Next steps

Follow the remaining steps of the [Getting Started guide](https://docs.meltano.com/getting-started.html):

1. [Select entities and attributes to extract](https://docs.meltano.com/getting-started.html#select-entities-and-attributes-to-extract)
1. [Add a loader to send data to a destination](https://docs.meltano.com/getting-started.html#add-a-loader-to-send-data-to-a-destination)
1. [Run a data integration (EL) pipeline](https://docs.meltano.com/getting-started.html#run-a-data-integration-el-pipeline)

If you run into any issues, [learn how to get help](https://docs.meltano.com/getting-help.html).

## Settings

`tap-spreadsheets-anywhere` requires the [configuration](https://docs.meltano.com/configuration.html) of the following settings:

- [Tables](#tables)

#### Minimal configuration

A minimal configuration of `tap-spreadsheets-anywhere` in your [`meltano.yml` project file](https://docs.meltano.com/concepts/project#meltano-yml-project-file) will look like this:

```yml{5-19}
plugins:
  extractors:
  - name: tap-spreadsheets-anywhere
    variant: etc
    config:
      tables:
        - path: s3://my-s3-bucket
          name: target_table_name
          pattern: "subfolder/common_prefix.*"
          start_date: "2017-05-01T00:00:00Z"
          key_properties: []
          format: csv
        - path: file:///home/user/Downloads/xls_files
          name: another_table_name
          pattern: "subdir/.*User.*"
          start_date: "2017-05-01T00:00:00Z"
          key_properties: [id]
          format: excel
          worksheet_name: Names
```

### Tables

- Name: `tables`
- [Environment variable](https://docs.meltano.com/configuration.html#configuring-settings): `TAP_SPREADSHEETS_ANYWHERE_TABLES`

Array holding objects that each describe a set of targeted source files.

See <https://github.com/ets/tap-spreadsheets-anywhere#configuration>.

#### How to use

Manage this setting directly in your [`meltano.yml` project file](https://docs.meltano.com/concepts/project#meltano-yml-project-file):

```yml{5-13}
plugins:
  extractors:
  - name: tap-spreadsheets-anywhere
    variant: etc
    config:
      tables:
        - path: <path>
          name: <table_name>
          pattern: "<pattern>"
          start_date: "YYYY-MM-DDTHH:MM:SSZ"
          key_properties: [<key>]
          format: <csv|excel>
        # ...
```

Alternatively, manage this setting using [`meltano config`](https://docs.meltano.com/command-line-interface.html#config) or an [environment variable](https://docs.meltano.com/configuration.html#configuring-settings):

```bash
meltano config tap-spreadsheets-anywhere set tables '[{"path": "<path>", ...}, ...]'

export TAP_SPREADSHEETS_ANYWHERE_TABLES='[{"path": "<path>", ...}, ...]'
```
