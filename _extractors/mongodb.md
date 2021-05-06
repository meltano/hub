---
layout: page
description: Use Meltano to pull data from a MongoDB database and load it into Snowflake, PostgreSQL, and more
---

# MongoDB

The `tap-mongodb` [extractor](https://meltano.com/plugins/extractors/) pulls data from a [MongoDB](https://www.mongodb.com/) database.

- **Repository**: <https://github.com/singer-io/tap-mongodb>
- **Maintainer**: [Stitch](https://www.stitchdata.com/)
- **Maintenance status**: Unresponsive to community issues and contributions
  - A [more active fork](https://github.com/singer-io/tap-mongodb/network) may be available that you can [use instead](https://meltano.com/docs/plugin-management.html#using-a-custom-fork-of-a-plugin).
  - This plugin is [up for adoption](https://meltano.com/docs/contributor-guide.html#adopting-a-plugin)!

## Getting Started

### Prerequisites

If you haven't already, follow the initial steps of the [Getting Started guide](https://meltano.com/docs/getting-started.html):

1. [Install Meltano](https://meltano.com/docs/getting-started.html#install-meltano)
1. [Create your Meltano project](https://meltano.com/docs/getting-started.html#create-your-meltano-project)

### Installation and configuration

#### Using the Command Line Interface

1. Add the `tap-mongodb` extractor to your project using [`meltano add`](https://meltano.com/docs/command-line-interface.html#add):

    ```bash
    meltano add extractor tap-mongodb
    ```

1. Configure the [settings](#settings) below using [`meltano config`](https://meltano.com/docs/command-line-interface.html#config).

#### Using Meltano UI

1. Start [Meltano UI](https://meltano.com/docs/ui.html) using [`meltano ui`](https://meltano.com/docs/command-line-interface.html#ui):

    ```bash
    meltano ui
    ```

1. Open the Extractors interface at <http://localhost:5000/extractors>.
1. Click the "Add to project" button for "MongoDB".
1. Configure the [settings](#settings) below in the "Configuration" interface that opens automatically.

### Next steps

Follow the remaining steps of the [Getting Started guide](https://meltano.com/docs/getting-started.html):

1. [Select entities and attributes to extract](https://meltano.com/docs/getting-started.html#select-entities-and-attributes-to-extract)
1. [Choose how to replicate each entity](https://meltano.com/docs/getting-started.html#choose-how-to-replicate-each-entity)

    Supported [replication methods](https://meltano.com/docs/integration.html#replication-methods):
    [`LOG_BASED`](https://meltano.com/docs/integration.html#log-based-incremental-replication),
    [`FULL_TABLE`](https://meltano.com/docs/integration.html#full-table-replication)

1. [Add a loader to send data to a destination](https://meltano.com/docs/getting-started.html#add-a-loader-to-send-data-to-a-destination)
1. [Run a data integration (EL) pipeline](https://meltano.com/docs/getting-started.html#run-a-data-integration-el-pipeline)

If you run into any issues, [learn how to get help](https://meltano.com/docs/getting-help.html).

## Settings

`tap-mongodb` requires the [configuration](https://meltano.com/docs/configuration.html) of the following settings:

- [Host](#host)
- [Port](#port)
- [User](#user)
- [Password](#password)
- [Database](#database)

#### Minimal configuration

A minimal configuration of `tap-mongodb` in your [`meltano.yml` project file](https://meltano.com/docs/project.html#meltano-yml-project-file) will look like this:

```yml{5-9}
plugins:
  extractors:
  - name: tap-mongodb
    variant: singer-io
    config:
      host: mongodb.example.com
      port: 27017
      user: my_user
      database: my_database
```

Sensitive values are most appropriately stored in [the environment](https://meltano.com/docs/configuration.html#configuring-settings) or your project's [`.env` file](https://meltano.com/docs/project.html#env):

```bash
export TAP_MONGODB_PASSWORD=my_password
```

### Host

- Name: `host`
- [Environment variable](https://meltano.com/docs/configuration.html#configuring-settings): `TAP_MONGODB_HOST`
- Default: `localhost`

#### How to use

Manage this setting using [Meltano UI](#using-meltano-ui), [`meltano config`](https://meltano.com/docs/command-line-interface.html#config), or an [environment variable](https://meltano.com/docs/configuration.html#configuring-settings):

```bash
meltano config tap-mongodb set host <host>

export TAP_MONGODB_HOST=<host>
```

### Port

- Name: `port`
- [Environment variable](https://meltano.com/docs/configuration.html#configuring-settings): `TAP_MONGODB_PORT`
- Default: `27017`

#### How to use

Manage this setting using [Meltano UI](#using-meltano-ui), [`meltano config`](https://meltano.com/docs/command-line-interface.html#config), or an [environment variable](https://meltano.com/docs/configuration.html#configuring-settings):

```bash
meltano config tap-mongodb set port 27018

export TAP_MONGODB_PORT=27018
```

### User

- Name: `user`
- [Environment variable](https://meltano.com/docs/configuration.html#configuring-settings): `TAP_MONGODB_USER`

#### How to use

Manage this setting using [Meltano UI](#using-meltano-ui), [`meltano config`](https://meltano.com/docs/command-line-interface.html#config), or an [environment variable](https://meltano.com/docs/configuration.html#configuring-settings):

```bash
meltano config tap-mongodb set user <user>

export TAP_MONGODB_USER=<user>
```

### Password

- Name: `password`
- [Environment variable](https://meltano.com/docs/configuration.html#configuring-settings): `TAP_MONGODB_PASSWORD`

#### How to use

Manage this setting using [Meltano UI](#using-meltano-ui), [`meltano config`](https://meltano.com/docs/command-line-interface.html#config), or an [environment variable](https://meltano.com/docs/configuration.html#configuring-settings):

```bash
meltano config tap-mongodb set password <password>

export TAP_MONGODB_PASSWORD=<password>
```

### Database

- Name: `database`
- [Environment variable](https://meltano.com/docs/configuration.html#configuring-settings): `TAP_MONGODB_DATABASE`

This is the database used for authentication, not the database used for extraction.
The data extracted is determined by following the [selecting entities and attributes](https://meltano.com/docs/getting-started.html#select-entities-and-attributes-to-extract) instructions.

#### How to use

Manage this setting using [Meltano UI](#using-meltano-ui), [`meltano config`](https://meltano.com/docs/command-line-interface.html#config), or an [environment variable](https://meltano.com/docs/configuration.html#configuring-settings):

```bash
meltano config tap-mongodb set database <database>

export TAP_MONGODB_DATABASE=<database>
```

### Replica Set

- Name: `replica_set`
- [Environment variable](https://meltano.com/docs/configuration.html#configuring-settings): `TAP_MONGODB_REPLICA_SET`

#### How to use

Manage this setting using [Meltano UI](#using-meltano-ui), [`meltano config`](https://meltano.com/docs/command-line-interface.html#config), or an [environment variable](https://meltano.com/docs/configuration.html#configuring-settings):

```bash
meltano config tap-mongodb set replica_set <replica_set>

export TAP_MONGODB_REPLICA_SET=<replica_set>
```

### SSL

- Name: `ssl`
- [Environment variable](https://meltano.com/docs/configuration.html#configuring-settings): `TAP_MONGODB_SSL`
- Default: `false`

#### How to use

Manage this setting using [Meltano UI](#using-meltano-ui), [`meltano config`](https://meltano.com/docs/command-line-interface.html#config), or an [environment variable](https://meltano.com/docs/configuration.html#configuring-settings):

```bash
meltano config tap-mongodb set ssl true

export TAP_MONGODB_SSL=true
```

### Verify Mode

- Name: `verify_mode`
- [Environment variable](https://meltano.com/docs/configuration.html#configuring-settings): `TAP_MONGODB_VERIFY_MODE`
- Default: `true`

SSL verify mode

#### How to use

Manage this setting using [Meltano UI](#using-meltano-ui), [`meltano config`](https://meltano.com/docs/command-line-interface.html#config), or an [environment variable](https://meltano.com/docs/configuration.html#configuring-settings):

```bash
meltano config tap-mongodb set verify_mode false

export TAP_MONGODB_VERIFY_MODE=false
```

### Include Schemas In Destination Stream Name

- Name: `include_schemas_in_destination_stream_name`
- [Environment variable](https://meltano.com/docs/configuration.html#configuring-settings): `TAP_MONGODB_INCLUDE_SCHEMAS_IN_DESTINATION_STREAM_NAME`
- Default: `false`

Forces the stream names to take the form `<database_name>_<collection_name>` instead of `<collection_name>`

#### How to use

Manage this setting using [Meltano UI](#using-meltano-ui), [`meltano config`](https://meltano.com/docs/command-line-interface.html#config), or an [environment variable](https://meltano.com/docs/configuration.html#configuring-settings):

```bash
meltano config tap-mongodb set include_schemas_in_destination_stream_name true

export TAP_MONGODB_INCLUDE_SCHEMAS_IN_DESTINATION_STREAM_NAME=true
```
