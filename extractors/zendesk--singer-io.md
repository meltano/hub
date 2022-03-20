---
title: Zendesk (`singer-io` variant)
layout: plugin_page
description: Use Meltano to pull data from the Zendesk API and load it into Snowflake, PostgreSQL, and more
---


The `tap-zendesk` [extractor](https://meltano.com/plugins/extractors/) pulls data from the [Zendesk API](https://developer.zendesk.com/rest_api).

- **Repository**: <https://github.com/singer-io/tap-zendesk>
- **Maintainer**: [Stitch](https://www.stitchdata.com/)
- **Maintenance status**: Nonresponsive to community issues and contributions
  - A [more active alternative variant](#alternative-variants) is available.

#### Alternative variants

Multiple [variants](https://docs.meltano.com/plugins.html#variants) of `tap-zendesk` are available.
This document describes the `singer-io` variant.

Alternative option is [`twilio-labs`](./zendesk.html) (default).

## Getting Started

### Prerequisites

If you haven't already, follow the initial steps of the [Getting Started guide](https://docs.meltano.com/getting-started.html):

1. [Install Meltano](https://docs.meltano.com/getting-started.html#install-meltano)
1. [Create your Meltano project](https://docs.meltano.com/getting-started.html#create-your-meltano-project)

### Installation and configuration

#### Using the Command Line Interface

1. Add the `singer-io` variant of `tap-zendesk` extractor to your project using [`meltano add`](https://docs.meltano.com/command-line-interface.html#add):

    ```bash
    meltano add extractor tap-zendesk --variant singer-io
    ```

1. Configure the [settings](#settings) below using [`meltano config`](https://docs.meltano.com/command-line-interface.html#config).

#### Using Meltano UI

1. Start [Meltano UI](https://docs.meltano.com/ui.html) using [`meltano ui`](https://docs.meltano.com/command-line-interface.html#ui):

    ```bash
    meltano ui
    ```

1. Open the Extractors interface at <http://localhost:5000/extractors>.
1. Click the "Add to project" button for "Zendesk".
1. Choose "Add variant 'singer-io'".
1. Configure the [settings](#settings) below in the "Configuration" interface that opens automatically.

### Next steps

Follow the remaining steps of the [Getting Started guide](https://docs.meltano.com/getting-started.html):

1. [Select entities and attributes to extract](https://docs.meltano.com/getting-started.html#select-entities-and-attributes-to-extract)
1. [Add a loader to send data to a destination](https://docs.meltano.com/getting-started.html#add-a-loader-to-send-data-to-a-destination)
1. [Run a data integration (EL) pipeline](https://docs.meltano.com/getting-started.html#run-a-data-integration-el-pipeline)

If you run into any issues, [learn how to get help](https://docs.meltano.com/getting-help.html).

## Settings

`tap-zendesk` requires the [configuration](https://docs.meltano.com/configuration.html) of the following settings:

In case of API token authentication:

- [Email](#email)
- [API Token](#api-token)

In case of OAuth authentication:

- [Access Token](#access-token)

Always:

- [Subdomain](#subdomain)
- [Start Date](#start-date)

These and other supported settings are documented below.
To quickly find the setting you're looking for, use the Table of Contents in the sidebar.

#### Minimal configuration

A minimal configuration of `tap-zendesk` in your [`meltano.yml` project file](https://docs.meltano.com/project.html#meltano-yml-project-file) will look like this:

```yml{5-8}
plugins:
  extractors:
  - name: tap-zendesk
    variant: singer-io
    config:
      email: user@example.com
      subdomain: my_subdomain
      start_date: '2020-10-01T00:00:00Z'
```

Sensitive values are most appropriately stored in [the environment](https://docs.meltano.com/configuration.html#configuring-settings) or your project's [`.env` file](https://docs.meltano.com/project.html#env):

```bash
export TAP_ZENDESK_API_TOKEN=my_api_token
```

### Email

- Name: `email`
- [Environment variable](https://docs.meltano.com/configuration.html#configuring-settings): `TAP_ZENDESK_EMAIL`

This is the email you use to login to your Zendesk dashboard.

Not necessary when using OAuth authentication and setting [Access Token](#access-token).

#### How to use

Manage this setting using [Meltano UI](#using-meltano-ui), [`meltano config`](https://docs.meltano.com/command-line-interface.html#config), or an [environment variable](https://docs.meltano.com/configuration.html#configuring-settings):

```bash
meltano config tap-zendesk set email <email>

export TAP_ZENDESK_EMAIL=<email>
```

### API Token

- Name: `api_token`
- [Environment variable](https://docs.meltano.com/configuration.html#configuring-settings): `TAP_ZENDESK_API_TOKEN`

You can use the API Token authentication which can be generated from the Zendesk Admin page.

See <https://support.zendesk.com/hc/en-us/articles/226022787-Generating-a-new-API-token->.

#### How to get

1. Login to your Zendesk dashboard.

![Screenshot of sample Zendesk dashboard](/assets/images/tap-zendesk/01-zendesk-docs.png)

2. On the left navigation, scroll down to the `Channels` section to click on the `API` link. If you don't see this, your account does not have adequate permissions.

![Screenshot of left nav with API link](/assets/images/tap-zendesk/02-zendesk-docs.png)

3. Ensure that `Token Access` is enabled

4. Click on the `+` button to create a new API token

![Screenshot of new API token creation](/assets/images/tap-zendesk/03-zendesk-docs.png)

5. Add `Meltano` as the API Token Description

6. Copy the API token since it will not be shown again

7. Click `Save` button to complete API key creation

#### How to use

Manage this setting using [Meltano UI](#using-meltano-ui), [`meltano config`](https://docs.meltano.com/command-line-interface.html#config), or an [environment variable](https://docs.meltano.com/configuration.html#configuring-settings):

```bash
meltano config tap-zendesk set api_token <token>

export TAP_ZENDESK_API_TOKEN=<token>
```

### Access Token

- Name: `access_token`
- [Environment variable](https://docs.meltano.com/configuration.html#configuring-settings): `TAP_ZENDESK_ACCESS_TOKEN`

To use OAuth, you will need to fetch an `access_token` from a configured Zendesk integration.

See <https://support.zendesk.com/hc/en-us/articles/203663836>.

#### How to use

Manage this setting using [Meltano UI](#using-meltano-ui), [`meltano config`](https://docs.meltano.com/command-line-interface.html#config), or an [environment variable](https://docs.meltano.com/configuration.html#configuring-settings):

```bash
meltano config tap-zendesk set access_token <token>

export TAP_ZENDESK_ACCESS_TOKEN=<token>
```

### Subdomain

- Name: `subdomain`
- [Environment variable](https://docs.meltano.com/configuration.html#configuring-settings): `TAP_ZENDESK_SUBDOMAIN`

When visiting your Zendesk instance, the URL is structured as follows: `SUBDOMAIN.zendesk.com`.

You'll need this subdomain when configuring the extractor.

For example, if the URL is `meltano.zendesk.com`, then the subdomain is `meltano`.

#### How to use

Manage this setting using [Meltano UI](#using-meltano-ui), [`meltano config`](https://docs.meltano.com/command-line-interface.html#config), or an [environment variable](https://docs.meltano.com/configuration.html#configuring-settings):

```bash
meltano config tap-zendesk set subdomain <subdomain>

export TAP_ZENDESK_SUBDOMAIN=<subdomain>
```

### Start Date

- Name: `start_date`
- [Environment variable](https://docs.meltano.com/configuration.html#configuring-settings): `TAP_ZENDESK_START_DATE`

This property determines how much historical data will be extracted.

Please be aware that the larger the time period and amount of data, the longer the initial extraction can be expected to take.

#### How to use

Manage this setting using [Meltano UI](#using-meltano-ui), [`meltano config`](https://docs.meltano.com/command-line-interface.html#config), or an [environment variable](https://docs.meltano.com/configuration.html#configuring-settings):

```bash
meltano config tap-zendesk set start_date YYYY-MM-DDTHH:MM:SSZ

export TAP_ZENDESK_START_DATE=YYYY-MM-DDTHH:MM:SSZ

# For example:
meltano config tap-zendesk set start_date 2020-10-01T00:00:00Z

export TAP_ZENDESK_START_DATE=2020-10-01T00:00:00Z
```
