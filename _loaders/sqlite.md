---
layout: page
description: Use Meltano to pull data from various sources and load it into SQLite
---

# SQLite

The `target-sqlite` [loader](https://meltano.com/plugins/loaders/) loads [extracted](https://meltano.com/plugins/extractors/) data into a [SQLite](https://www.sqlite.org/) database.

- **Repository**: <https://gitlab.com/meltano/target-sqlite>
- **Maintainer**: Meltano community
- **Maintenance status**: Active

## Getting Started

### Prerequisites

If you haven't already, follow the initial steps of the [Getting Started guide](https://meltano.com/docs/getting-started.html):

1. [Install Meltano](https://meltano.com/docs/getting-started.html#install-meltano)
1. [Create your Meltano project](https://meltano.com/docs/getting-started.html#create-your-meltano-project)
1. [Add an extractor to pull data from a source](https://meltano.com/docs/getting-started.html#add-an-extractor-to-pull-data-from-a-source)

### Installation and configuration

#### Using the Command Line Interface

1. Add the `target-sqlite` loader to your project using [`meltano add`](https://meltano.com/docs/command-line-interface.html#add):

    ```bash
    meltano add loader target-sqlite
    ```

1. Configure the [settings](#settings) below using [`meltano config`](https://meltano.com/docs/command-line-interface.html#config).

#### Using Meltano UI

1. Start [Meltano UI](https://meltano.com/docs/ui.html) using [`meltano ui`](https://meltano.com/docs/command-line-interface.html#ui):

    ```bash
    meltano ui
    ```

1. Open the Loaders interface at <http://localhost:5000/loaders>.
1. Click the "Add to project" button for "SQLite".
1. Configure the [settings](#settings) below in the "Configuration" interface that opens automatically.

### Next steps

Follow the remaining step of the [Getting Started guide](https://meltano.com/docs/getting-started.html):

1. [Run a data integration (EL) pipeline](https://meltano.com/docs/getting-started.html#run-a-data-integration-el-pipeline)

If you run into any issues, [learn how to get help](https://meltano.com/docs/getting-help.html).

## Settings

`target-sqlite` requires the [configuration](https://meltano.com/docs/configuration.html) of the following settings:

- [Database](#database)

These and other supported settings are documented below.
To quickly find the setting you're looking for, use the Table of Contents in the sidebar.

#### Minimal configuration

A minimal configuration of `target-sqlite` in your [`meltano.yml` project file](https://meltano.com/docs/project.html#meltano-yml-project-file) will look like this:

```yml{5-6}
plugins:
  loaders:
  - name: target-sqlite
    variant: meltano
    config:
      database: my_database.db
```

### Database

- Name: `database`
- [Environment variable](https://meltano.com/docs/configuration.html#configuring-settings): `TARGET_SQLITE_DATABASE`, alias: `SQLITE_DATABASE`
- Default: `warehouse`

Name of the SQLite database file to be used or created, relative to the project root.

The `.db` extension is optional and will be added automatically when omitted.

#### How to use

Manage this setting using [Meltano UI](#using-meltano-ui), [`meltano config`](https://meltano.com/docs/command-line-interface.html#config), or an [environment variable](https://meltano.com/docs/configuration.html#configuring-settings):

```bash
meltano config target-sqlite set database <database>

export TARGET_SQLITE_DATABASE=<database>
```

### Batch Size

- Name: `batch_size`
- [Environment variable](https://meltano.com/docs/configuration.html#configuring-settings): `TARGET_SQLITE_BATCH_SIZE`
- Default: `50`

How many records are sent to SQLite at a time?

#### How to use

Manage this setting using [Meltano UI](#using-meltano-ui), [`meltano config`](https://meltano.com/docs/command-line-interface.html#config), or an [environment variable](https://meltano.com/docs/configuration.html#configuring-settings):

```bash
meltano config target-sqlite set batch_size 100

export TARGET_SQLITE_BATCH_SIZE=100
```

### Timestamp Column

- Name: `timestamp_column`
- [Environment variable](https://meltano.com/docs/configuration.html#configuring-settings): `TARGET_SQLITE_TIMESTAMP_COLUMN`
- Default: `__loaded_at`

Name of the column used for recording the timestamp when Data are loaded to SQLite.

#### How to use

Manage this setting using [Meltano UI](#using-meltano-ui), [`meltano config`](https://meltano.com/docs/command-line-interface.html#config), or an [environment variable](https://meltano.com/docs/configuration.html#configuring-settings):

```bash
meltano config target-sqlite set timestamp_column <column>

export TARGET_SQLITE_TIMESTAMP_COLUMN=<column>
```
