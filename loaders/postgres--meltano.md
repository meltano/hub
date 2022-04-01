---
title: PostgreSQL (`meltano` variant)
layout: plugin_page
description: Use Meltano to pull data from various sources and load it into PostgreSQL
---

The `target-postgres` [loader](https://meltano.com/plugins/loaders/) loads [extracted](https://meltano.com/plugins/extractors/) data into a [PostgreSQL](https://www.postgresql.org/) database.

- **Repository**: <https://github.com/meltano/target-postgres>
- **Maintainer**: Meltano Community
- **Maintenance status**: Active

#### Alternative variants

Multiple [variants](https://docs.meltano.com/concepts/plugins#variants) of `target-postgres` are available.
This document describes the `meltano` variant.

Alternative options are [`transferwise`](./postgres.html) (default) and [`datamill-co`](./postgres--datamill-co.html).

## Getting Started

### Prerequisites

If you haven't already, follow the initial steps of the [Getting Started guide](https://docs.meltano.com/getting-started.html):

1. [Install Meltano](https://docs.meltano.com/getting-started.html#install-meltano)
1. [Create your Meltano project](https://docs.meltano.com/getting-started.html#create-your-meltano-project)
1. [Add an extractor to pull data from a source](https://docs.meltano.com/getting-started.html#add-an-extractor-to-pull-data-from-a-source)

### Installation and configuration

#### Using the Command Line Interface

1. Add the `meltano` variant of the `target-postgres` loader to your project using [`meltano add`](https://docs.meltano.com/command-line-interface.html#add):

    ```bash
    meltano add loader target-postgres --variant meltano
    ```

1. Configure the [settings](#settings) below using [`meltano config`](https://docs.meltano.com/command-line-interface.html#config).

#### Using Meltano UI

1. Start [Meltano UI](https://docs.meltano.com/ui.html) using [`meltano ui`](https://docs.meltano.com/command-line-interface.html#ui):

    ```bash
    meltano ui
    ```

1. Open the Loaders interface at <http://localhost:5000/loaders>.
1. Click the arrow next to the "Add to project" button for "PostgreSQL".
1. Choose "Add variant 'meltano'".
1. Configure the [settings](#settings) below in the "Configuration" interface that opens automatically.

### Next steps

Follow the remaining step of the [Getting Started guide](https://docs.meltano.com/getting-started.html):

1. [Run a data integration (EL) pipeline](https://docs.meltano.com/getting-started.html#run-a-data-integration-el-pipeline)

If you run into any issues, refer to the ["Troubleshooting" section](#troubleshooting) below or [learn how to get help](https://docs.meltano.com/getting-help.html).

## Settings

`target-postgres` requires the [configuration](https://docs.meltano.com/configuration.html) of the following settings:

- [User](#user)
- [Password](#password)
- [Host](#host)
- [Port](#port)
- [DBname](#dbname)
- [Schema](#schema)

A [URL](#url) setting is also available that can be used as an alternative to setting User, Password, Host, Port, and DBname separately.

These and other supported settings are documented below.
To quickly find the setting you're looking for, use the Table of Contents in the sidebar.

#### Minimal configuration

A minimal configuration of `target-postgres` in your [`meltano.yml` project file](https://docs.meltano.com/concepts/project#meltano-yml-project-file) will look like this:

```yml{5-10}
plugins:
  loaders:
  - name: target-postgres
    variant: meltano
    config:
      user: my_user
      host: postgres.example.com
      port: 5432
      dbname: my_database
      # schema: my_schema   # override if default (see below) is not appropriate
```

Sensitive values are most appropriately stored in [the environment](https://docs.meltano.com/configuration.html#configuring-settings) or your project's [`.env` file](https://docs.meltano.com/concepts/project#env):

```bash
export TARGET_POSTGRES_PASSWORD=my_password
```

### User

- Name: `user`
- [Environment variable](https://docs.meltano.com/configuration.html#configuring-settings): `TARGET_POSTGRES_USER`, alias: `PG_USERNAME`, `POSTGRES_USER`
- Default: `warehouse`

#### How to use

Manage this setting using [Meltano UI](#using-meltano-ui), [`meltano config`](https://docs.meltano.com/command-line-interface.html#config), or an [environment variable](https://docs.meltano.com/configuration.html#configuring-settings):

```bash
meltano config target-postgres set user <user>

export TARGET_POSTGRES_USER=<user>
```

### Password

- Name: `password`
- [Environment variable](https://docs.meltano.com/configuration.html#configuring-settings): `TARGET_POSTGRES_PASSWORD`, alias: `PG_PASSWORD`, `POSTGRES_PASSWORD`
- Default: `warehouse`

#### How to use

Manage this setting using [Meltano UI](#using-meltano-ui), [`meltano config`](https://docs.meltano.com/command-line-interface.html#config), or an [environment variable](https://docs.meltano.com/configuration.html#configuring-settings):

```bash
meltano config target-postgres set password <password>

export TARGET_POSTGRES_PASSWORD=<password>
```

### Host

- Name: `host`
- [Environment variable](https://docs.meltano.com/configuration.html#configuring-settings): `TARGET_POSTGRES_HOST`, alias: `PG_ADDRESS`, `POSTGRES_HOST`
- Default: `localhost`

#### How to use

Manage this setting using [Meltano UI](#using-meltano-ui), [`meltano config`](https://docs.meltano.com/command-line-interface.html#config), or an [environment variable](https://docs.meltano.com/configuration.html#configuring-settings):

```bash
meltano config target-postgres set host <host>

export TARGET_POSTGRES_HOST=<host>
```

### Port

- Name: `port`
- [Environment variable](https://docs.meltano.com/configuration.html#configuring-settings): `TARGET_POSTGRES_PORT`, alias: `PG_PORT`, `POSTGRES_PORT`
- Default: `5502`

#### How to use

Manage this setting using [Meltano UI](#using-meltano-ui), [`meltano config`](https://docs.meltano.com/command-line-interface.html#config), or an [environment variable](https://docs.meltano.com/configuration.html#configuring-settings):

```bash
meltano config target-postgres set port 5432

export TARGET_POSTGRES_PORT=5432
```

### DBname

- Name: `dbname`
- [Environment variable](https://docs.meltano.com/configuration.html#configuring-settings): `TARGET_POSTGRES_DBNAME`, alias: `PG_DATABASE`, `POSTGRES_DBNAME`
- Default: `warehouse`

#### How to use

Manage this setting using [Meltano UI](#using-meltano-ui), [`meltano config`](https://docs.meltano.com/command-line-interface.html#config), or an [environment variable](https://docs.meltano.com/configuration.html#configuring-settings):

```bash
meltano config target-postgres set dbname <database>

export TARGET_POSTGRES_DBNAME=<database>
```

### URL

- Name: `url`
- [Environment variable](https://docs.meltano.com/configuration.html#configuring-settings): `TARGET_POSTGRES_URL`, alias: `PG_URL`, `POSTGRES_URL`

Lets you set [User](#user), [Password](#password), [Host](#host), [Port](#port), and [DBname](#dbname) in one go using a [`postgresql://` URI](https://docs.sqlalchemy.org/en/13/core/engines.html#postgresql).

Takes precedence over the other settings when set.

#### How to use

Manage this setting using [Meltano UI](#using-meltano-ui), [`meltano config`](https://docs.meltano.com/command-line-interface.html#config), or an [environment variable](https://docs.meltano.com/configuration.html#configuring-settings):

```bash
meltano config target-postgres set url postgresql://<username>:<password>@<host>:<port>/<database>

export TARGET_POSTGRES_URL=postgresql://<username>:<password>@<host>:<port>/<database>
```

### Schema

- Name: `schema`
- [Environment variable](https://docs.meltano.com/configuration.html#configuring-settings): `TARGET_POSTGRES_SCHEMA`, alias: `PG_SCHEMA`, `POSTGRES_SCHEMA`
- Default: `$MELTANO_EXTRACT__LOAD_SCHEMA`, which [will expand to](https://docs.meltano.com/configuration.html#expansion-in-setting-values) the value of the [`load_schema` extra](https://docs.meltano.com/concepts/plugins#load-schema-extra) for the extractor used in the pipeline, which defaults to the extractor's namespace, e.g. `tap_gitlab` for [`tap-gitlab`](https://meltano.com/plugins/extractors/gitlab.html).

#### How to use

Manage this setting using [Meltano UI](#using-meltano-ui), [`meltano config`](https://docs.meltano.com/command-line-interface.html#config), or an [environment variable](https://docs.meltano.com/configuration.html#configuring-settings):

```bash
meltano config target-postgres set schema <schema>

export TARGET_POSTGRES_SCHEMA=<schema>
```

## Troubleshooting

### Error: `ld: library not found for -lssl` or `clang: error: linker command failed with exit code 1` or `error: command 'clang' failed with exit status 1`

This error message indicates that there is a problem installing OpenSSL. This
[Stack Overflow answer](https://stackoverflow.com/questions/26288042/error-installing-psycopg2-library-not-found-for-lssl)
has specific recommendations on setting the `LDFLAGS` and/or `CPPFLAGS` environment variables.
Set those prior to running `meltano add loader target-postgres --variant meltano`.
