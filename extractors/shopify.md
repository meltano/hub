---
title: Shopify
layout: plugin_page
description: Use Meltano to pull data from the Shopify API and load it into Snowflake, PostgreSQL, and more
---


The `tap-shopify` [extractor](https://meltano.com/plugins/extractors/) pulls data from the [Shopify API](https://shopify.dev/docs/admin-api/rest/reference).

- **Repository**: <https://github.com/singer-io/tap-shopify>
- **Maintainer**: [Stitch](https://www.stitchdata.com/)
- **Maintenance status**: Unresponsive to community issues and contributions
  - A [more active fork](https://github.com/singer-io/tap-shopify/network) may be available that you can [use instead](https://docs.meltano.com/plugin-management.html#using-a-custom-fork-of-a-plugin).
  - This plugin is [up for adoption](https://docs.meltano.com/contributor-guide.html#adopting-a-plugin)!

## Getting Started

### Prerequisites

If you haven't already, follow the initial steps of the [Getting Started guide](https://docs.meltano.com/getting-started.html):

1. [Install Meltano](https://docs.meltano.com/getting-started.html#install-meltano)
1. [Create your Meltano project](https://docs.meltano.com/getting-started.html#create-your-meltano-project)

### Installation and configuration

#### Using the Command Line Interface

1. Add the `tap-shopify` extractor to your project using [`meltano add`](https://docs.meltano.com/command-line-interface.html#add):

    ```bash
    meltano add extractor tap-shopify
    ```

1. Configure the [settings](#settings) below using [`meltano config`](https://docs.meltano.com/command-line-interface.html#config).

#### Using Meltano UI

1. Start [Meltano UI](https://docs.meltano.com/ui.html) using [`meltano ui`](https://docs.meltano.com/command-line-interface.html#ui):

    ```bash
    meltano ui
    ```

1. Open the Extractors interface at <http://localhost:5000/extractors>.
1. Click the "Add to project" button for "Shopify".
1. Configure the [settings](#settings) below in the "Configuration" interface that opens automatically.

### Next steps

Follow the remaining steps of the [Getting Started guide](https://docs.meltano.com/getting-started.html):

1. [Select entities and attributes to extract](https://docs.meltano.com/getting-started.html#select-entities-and-attributes-to-extract)
1. [Add a loader to send data to a destination](https://docs.meltano.com/getting-started.html#add-a-loader-to-send-data-to-a-destination)
1. [Run a data integration (EL) pipeline](https://docs.meltano.com/getting-started.html#run-a-data-integration-el-pipeline)

If you run into any issues, [learn how to get help](https://docs.meltano.com/getting-help.html).

## Settings

`tap-shopify` requires the [configuration](https://docs.meltano.com/configuration.html) of the following settings:

- [Shop](#shop)
- [API Key](#api-key)
- [Start Date](#start-date)

These and other supported settings are documented below.
To quickly find the setting you're looking for, use the Table of Contents in the sidebar.

#### Minimal configuration

A minimal configuration of `tap-shopify` in your [`meltano.yml` project file](https://docs.meltano.com/project.html#meltano-yml-project-file) will look like this:

```yml{5-7}
plugins:
  extractors:
  - name: tap-shopify
    variant: singer-io
    config:
      shop: my_store_subdomain
      start_date: '2020-10-01T00:00:00Z'
```

Sensitive values are most appropriately stored in [the environment](https://docs.meltano.com/configuration.html#configuring-settings) or your project's [`.env` file](https://docs.meltano.com/project.html#env):

```bash
export TAP_SHOPIFY_API_KEY=my_key
```

### Shop

- Name: `shop`
- [Environment variable](https://docs.meltano.com/configuration.html#configuring-settings): `TAP_SHOPIFY_SHOP`

The store subdomain, which can be derived from your Shopify admin URL.

If your admin URL starts with `https://my-first-store.myshopify.com/`, your store subdomain is `my-first-store`.

#### How to use

Manage this setting using [Meltano UI](#using-meltano-ui), [`meltano config`](https://docs.meltano.com/command-line-interface.html#config), or an [environment variable](https://docs.meltano.com/configuration.html#configuring-settings):

```bash
meltano config tap-shopify set shop <subdomain>

export TAP_SHOPIFY_SHOP=<subdomain>
```

### API Key

- Name: `api_key`
- [Environment variable](https://docs.meltano.com/configuration.html#configuring-settings): `TAP_SHOPIFY_API_KEY`

A Private App API Password or API Key generated using OAuth

#### How to get

##### Create private app

First, you will need to create a [Private App](https://help.shopify.com/en/manual/apps/private-apps):

1. Log in to your Shopify store admin at `https://<store subdomain>.myshopify.com/admin`
2. Click "Apps" in the sidebar on the left
3. On the bottom of the page, click "Manage private apps" next to "Working with a developer on your shop?"
4. Click the "Create a new private app" button
5. Enter a "Private app name" of your choosing, e.g. "Meltano"
6. Enter your email address under "Emergency developer email"
7. In the "Admin API" section, click "▼ Review disabled Admin API permissions"
8. Choose "Read access" rather than "No access" in the access level dropdowns for the following permissions:
   1. Products, variants and collections - `read_products, write_products`
   2. Orders, transactions and fulfillments - `read_orders, write_orders`
   3. Customer details and customer groups - `read_customers, write_customers`
9. Click "Save"
10. In the modal that appears, click "I understand, create the app"

##### Find your API password

Now that your app has been created, we can acquire the password Meltano will use to authenticate with the Shopify API.

1. In the "Admin API" section on the private app details page, find the "Password" field and click "Show"
2. The value that appears (starting with `shppa_`) is your API password. You can copy and paste it into the Meltano data source configuration.

![Screenshot of Shopify interface showing private app API password](/assets/images/tap-shopify/private-app-api-password.png)

#### How to use

Manage this setting using [Meltano UI](#using-meltano-ui), [`meltano config`](https://docs.meltano.com/command-line-interface.html#config), or an [environment variable](https://docs.meltano.com/configuration.html#configuring-settings):

```bash
meltano config tap-shopify set api_key <key>

export TAP_SHOPIFY_API_KEY=<key>
```

### Start Date

- Name: `start_date`
- [Environment variable](https://docs.meltano.com/configuration.html#configuring-settings): `TAP_SHOPIFY_START_DATE`

This property determines how much historical data will be extracted.

Please be aware that the larger the time period and amount of data, the longer the initial extraction can be expected to take.

#### How to use

Manage this setting using [Meltano UI](#using-meltano-ui), [`meltano config`](https://docs.meltano.com/command-line-interface.html#config), or an [environment variable](https://docs.meltano.com/configuration.html#configuring-settings):

```bash
meltano config tap-shopify set start_date YYYY-MM-DDTHH:MM:SSZ

export TAP_SHOPIFY_START_DATE=YYYY-MM-DDTHH:MM:SSZ

# For example:
meltano config tap-shopify set start_date 2020-10-01T00:00:00Z

export TAP_SHOPIFY_START_DATE=2020-10-01T00:00:00Z
```
