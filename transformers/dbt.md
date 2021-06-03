---
title: dbt - data build tool
layout: plugin_page
description: Use Meltano to transform data in your warehouse using dbt
---

The `dbt` [transformer](https://meltano.com/docs/transforms.html/) uses SQL to transform data stored in your warehouse.

- **Repository**: <https://www.getdbt.com/>
- **Maintainer**: Fishtown Analytics
- **Maintenance status**: Active

## Getting Started

### Prerequisites

If you haven't already, follow the [Getting Started guide](https://meltano.com/docs/getting-started.html):

1. [Install Meltano](https://meltano.com/docs/getting-started.html#install-meltano)
1. [Create your Meltano project](https://meltano.com/docs/getting-started.html#create-your-meltano-project)
1. Load data into your warehouse by following the rest of the [Getting Started guide](https://meltano.com/docs/getting-started.html).

### Installation and configuration

#### Using the Command Line Interface

1. Add the `dbt` transformer to your project using [`meltano add`](https://meltano.com/docs/command-line-interface.html#add):

    ```bash
    meltano add transformer dbt
    ```

1. Configure the [settings](#settings) below using [`meltano config`](https://meltano.com/docs/command-line-interface.html#config).

### Next steps

1. [Transform loaded data for analysis](https://meltano.com/docs/getting-started.html#transform-loaded-data-for-analysis)

If you run into any issues, [learn how to get help](https://meltano.com/docs/getting-help.html).

## Settings

Meltano automatically defines all `dbt` settings. 
They can be [configured](https://meltano.com/docs/configuration.html) if needed. 
These settings are documented below.
To quickly find the setting you're looking for, use the Table of Contents at the top of the page.

#### Minimal configuration

A minimal configuration of `dbt` in your [`meltano.yml` project file](https://meltano.com/docs/project.html#meltano-yml-project-file) will look like this:

```yml{5-7}
plugins:
  transformers:
  - name: dbt
    pip_url: dbt==0.16.1
```

Sensitive values are most appropriately stored in [the environment](https://meltano.com/docs/configuration.html#configuring-settings) or your project's [`.env` file](https://meltano.com/docs/project.html#env):

### Project Directory

- Name: `project_dir`
- [Environment variable](https://meltano.com/docs/configuration.html#configuring-settings): `DBT_PROJECT_DIR`
- Default: `$MELTANO_PROJECT_ROOT/transform`

The directory where the dbt project is stored. The default value is the `/transform` directory in the Meltano project root directory.

#### How to use

Manage this setting using [Meltano UI](#using-meltano-ui), [`meltano config`](https://meltano.com/docs/command-line-interface.html#config), or an [environment variable](https://meltano.com/docs/configuration.html#configuring-settings):

```bash
meltano config dbt set project_dir <project_dir>

export DBT_PROJECT_DIR=<project_dir>
```


### Profiles Directory

- Name: `profiles_dir`
- [Environment variable](https://meltano.com/docs/configuration.html#configuring-settings): `DBT_PROFILES_DIR`
- Default: `$MELTANO_PROJECT_ROOT/transform/profile`

The directory where the dbt `profiles.yml` file is stored. 

#### How to use

Manage this setting using [Meltano UI](#using-meltano-ui), [`meltano config`](https://meltano.com/docs/command-line-interface.html#config), or an [environment variable](https://meltano.com/docs/configuration.html#configuring-settings):

```bash
meltano config dbt set profiles_dir <profiles_dir>

export DBT_PROFILES_DIR=<profiles_dir>
```

### Target Schema

- Name: `target_schema`
- [Environment variable](https://meltano.com/docs/configuration.html#configuring-settings): `DBT_TARGET_SCHEMA`
- Default: `analytics`

This is the schema dbt writes transformation results to.

#### How to use

Manage this setting using [Meltano UI](#using-meltano-ui), [`meltano config`](https://meltano.com/docs/command-line-interface.html#config), or an [environment variable](https://meltano.com/docs/configuration.html#configuring-settings):

```bash
meltano config dbt set target_schema <schema>

export DBT_TARGET_SCHEMA=<schema>
```


### Models

- Name: `models`
- [Environment variable](https://meltano.com/docs/configuration.html#configuring-settings): `DBT_MODELS`
- Default: `$MELTANO_TRANSFORM__PACKAGE_NAME $MELTANO_EXTRACTOR_NAMESPACE my_meltano_project`

This defines the list of models which dbt will run during a transformation.

#### How to use

Manage this setting using [Meltano UI](#using-meltano-ui), [`meltano config`](https://meltano.com/docs/command-line-interface.html#config), or an [environment variable](https://meltano.com/docs/configuration.html#configuring-settings):

```bash
meltano config dbt set models <models>

export DBT_MODELS=<models>
```


### Target

- Name: `target`
- [Environment variable](https://meltano.com/docs/configuration.html#configuring-settings): `DBT_TARGET`
- Default: `$MELTANO_LOAD__DIALECT`

This is the dialect of your warehouse where data is stored. It maps to the `type:` value in the dbt [`profiles.yml` file](https://docs.getdbt.com/dbt-cli/configure-your-profile).

#### How to use

This setting is managed by the loader and is not recommended to be changed via the transformer. You can, if needed, overwrite this setting using [Meltano UI](#using-meltano-ui), [`meltano config`](https://meltano.com/docs/command-line-interface.html#config), or an [environment variable](https://meltano.com/docs/configuration.html#configuring-settings):

```bash
meltano config dbt set target <target>

export DBT_TARGET=<target>
```


### Source Schema

- Name: `source_schema`
- [Environment variable](https://meltano.com/docs/configuration.html#configuring-settings): `DBT_SOURCE_SCHEMA`
- Default: `$MELTANO_LOAD__TARGET_SCHEMA`

This defines the schema were dbt will read data from.

#### How to use

This setting is managed by the loader and is not recommended to be changed via the transformer. You can, if needed, overwrite this setting using [Meltano UI](#using-meltano-ui), [`meltano config`](https://meltano.com/docs/command-line-interface.html#config), or an [environment variable](https://meltano.com/docs/configuration.html#configuring-settings):

```bash
meltano config dbt set source_schema <source_schema>

export DBT_SOURCE_SCHEMA=<source_schema>
```
