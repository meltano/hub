---
title: Marketo
layout: plugin_page
description: Use Meltano to pull data from the Marketo API and load it into Snowflake, PostgreSQL, and more
---


The `tap-marketo` [extractor](https://meltano.com/plugins/extractors/) pulls data from the [Marketo API](https://developers.marketo.com/rest-api/).

- **Repository**: <https://github.com/singer-io/tap-marketo>
- **Maintainer**: [Stitch](https://www.stitchdata.com/)
- **Maintenance status**: Active

## Getting Started

### Prerequisites

If you haven't already, follow the initial steps of the [Getting Started guide](https://meltano.com/docs/getting-started.html):

1. [Install Meltano](https://meltano.com/docs/getting-started.html#install-meltano)
1. [Create your Meltano project](https://meltano.com/docs/getting-started.html#create-your-meltano-project)

### Installation and configuration

#### Using the Command Line Interface

1. Add the `tap-marketo` extractor to your project using [`meltano add`](https://meltano.com/docs/command-line-interface.html#add):

    ```bash
    meltano add extractor tap-marketo
    ```

1. Configure the [settings](#settings) below using [`meltano config`](https://meltano.com/docs/command-line-interface.html#config).

#### Using Meltano UI

1. Start [Meltano UI](https://meltano.com/docs/ui.html) using [`meltano ui`](https://meltano.com/docs/command-line-interface.html#ui):

    ```bash
    meltano ui
    ```

1. Open the Extractors interface at <http://localhost:5000/extractors>.
1. Click the "Add to project" button for "Marketo".
1. Configure the [settings](#settings) below in the "Configuration" interface that opens automatically.

### Next steps

Follow the remaining steps of the [Getting Started guide](https://meltano.com/docs/getting-started.html):

1. [Select entities and attributes to extract](https://meltano.com/docs/getting-started.html#select-entities-and-attributes-to-extract)
1. [Add a loader to send data to a destination](https://meltano.com/docs/getting-started.html#add-a-loader-to-send-data-to-a-destination)
1. [Run a data integration (EL) pipeline](https://meltano.com/docs/getting-started.html#run-a-data-integration-el-pipeline)

If you run into any issues, [learn how to get help](https://meltano.com/docs/getting-help.html).

## Settings

`tap-marketo` requires the [configuration](https://meltano.com/docs/configuration.html) of the following settings:

- [Endpoint](#endpoint)
- [Client ID](#client-id)
- [Client Secret](#client-secret)
- [Start Date](#start-date)

These and other supported settings are documented below.
To quickly find the setting you're looking for, use the Table of Contents in the sidebar.

#### Minimal configuration

A minimal configuration of `tap-marketo` in your [`meltano.yml` project file](https://meltano.com/docs/project.html#meltano-yml-project-file) will look like this:

```yml{5-9}
plugins:
  extractors:
  - name: tap-marketo
    variant: singer-io
    config:
      endpoint: https://284-RPR-133.mktorest.com/rest
      client_id: 70ee92a1-603f-44a8-97a3-e0e55d758d1b
      start_date: '2020-10-01T00:00:00Z'
```

Sensitive values are most appropriately stored in [the environment](https://meltano.com/docs/configuration.html#configuring-settings) or your project's [`.env` file](https://meltano.com/docs/project.html#env):

```bash
export TAP_MARKETO_CLIENT_SECRET=my_secret
```

### Endpoint

- Name: `endpoint`
- [Environment variable](https://meltano.com/docs/configuration.html#configuring-settings): `TAP_MARKETO_ENDPOINT`

Endpoint URL

See <https://developers.marketo.com/rest-api/base-url/>.

#### How to use

Manage this setting using [Meltano UI](#using-meltano-ui), [`meltano config`](https://meltano.com/docs/command-line-interface.html#config), or an [environment variable](https://meltano.com/docs/configuration.html#configuring-settings):

```bash
meltano config tap-marketo set endpoint <endpoint_url>

export TAP_MARKETO_ENDPOINT=<endpoint_url>
```

### Client ID

- Name: `client_id`
- [Environment variable](https://meltano.com/docs/configuration.html#configuring-settings): `TAP_MARKETO_CLIENT_ID`

See <https://developers.marketo.com/rest-api/authentication/>.

#### How to use

Manage this setting using [Meltano UI](#using-meltano-ui), [`meltano config`](https://meltano.com/docs/command-line-interface.html#config), or an [environment variable](https://meltano.com/docs/configuration.html#configuring-settings):

```bash
meltano config tap-marketo set client_id <client_id>

export TAP_MARKETO_CLIENT_ID=<client_id>
```

### Client Secret

- Name: `client_secret`
- [Environment variable](https://meltano.com/docs/configuration.html#configuring-settings): `TAP_MARKETO_CLIENT_SECRET`

See <https://developers.marketo.com/rest-api/authentication/>.

#### How to use

Manage this setting using [Meltano UI](#using-meltano-ui), [`meltano config`](https://meltano.com/docs/command-line-interface.html#config), or an [environment variable](https://meltano.com/docs/configuration.html#configuring-settings):

```bash
meltano config tap-marketo set client_secret <client_secret>

export TAP_MARKETO_CLIENT_SECRET=<client_secret>
```

### Start Date

- Name: `start_date`
- [Environment variable](https://meltano.com/docs/configuration.html#configuring-settings): `TAP_MARKETO_START_DATE`

This property determines how much historical data will be extracted.

Please be aware that the larger the time period and amount of data, the longer the initial extraction can be expected to take.

#### How to use

Manage this setting using [Meltano UI](#using-meltano-ui), [`meltano config`](https://meltano.com/docs/command-line-interface.html#config), or an [environment variable](https://meltano.com/docs/configuration.html#configuring-settings):

```bash
meltano config tap-marketo set start_date YYYY-MM-DDTHH:MM:SSZ

export TAP_MARKETO_START_DATE=YYYY-MM-DDTHH:MM:SSZ

# For example:
meltano config tap-marketo set start_date 2020-10-01T00:00:00Z

export TAP_MARKETO_START_DATE=2020-10-01T00:00:00Z
```
