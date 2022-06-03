---
title: dbt - data build tool
layout: plugin_page
description: Use Meltano to transform data in your warehouse using dbt
---

The [`dbt`](https://www.getdbt.com) [transformer](https://docs.meltano.com/transforms.html) uses SQL to transform data stored in your warehouse.

- **Repository**: <https://github.com/dbt-labs/dbt>
- **Documentation**: <https://docs.getdbt.com/>
- **Maintainer**: [dbt Labs](https://www.getdbt.com/dbt-labs/about-us/)
- **Maintenance status**: Active

## Getting Started

### Prerequisites

If you haven't already, follow the [Getting Started guide](https://docs.meltano.com/getting-started.html):

1. [Install Meltano](https://docs.meltano.com/getting-started.html#install-meltano)
1. [Create your Meltano project](https://docs.meltano.com/getting-started.html#create-your-meltano-project)
1. Load data into your warehouse by following the rest of the [Getting Started guide](https://docs.meltano.com/getting-started.html).

### Installation and configuration

1. Add the `dbt` transformer to your project using [`meltano add`](https://docs.meltano.com/command-line-interface.html#add):

    ```bash
    meltano add transformer dbt
    ```

1. Configure the [settings](#settings) below using [`meltano config`](https://docs.meltano.com/command-line-interface.html#config).

### Next steps

1. [Transform loaded data for analysis](https://docs.meltano.com/getting-started.html#transform-loaded-data-for-analysis)

If you run into any issues, chat with us in [#troubleshooting](https://meltano.slack.com/archives/C01TCRBBJD7) on [Slack](https://meltano.com/slack).

## Settings

Meltano automatically sets default values for all `dbt` settings that can be [overridden](https://docs.meltano.com/configuration.html) if needed. 
These settings are documented below.
To quickly find the setting you're looking for, use the Table of Contents at the top of the page.

Settings for `dbt` itself can be configured through [`dbt_project.yml`](https://docs.getdbt.com/reference/dbt_project.yml) as usual, which can be found at `transform/dbt_project.yml` in your Meltano project.

#### Minimal configuration

A minimal configuration of `dbt` in your [`meltano.yml` project file](https://docs.meltano.com/concepts/project#meltano-yml-project-file) will look like this:

```yml{5-7}
plugins:
  transformers:
  - name: dbt
    pip_url: dbt==0.21.0
```

### Project Directory

- Name: `project_dir`
- [Environment variable](https://docs.meltano.com/configuration.html#configuring-settings): `DBT_PROJECT_DIR`
- Default: `$MELTANO_PROJECT_ROOT/transform`

The directory where the dbt project is stored. The default value is the `/transform` directory in the Meltano project root directory.

#### How to use

Manage this setting using [`meltano config`](https://docs.meltano.com/command-line-interface.html#config) or an [environment variable](https://docs.meltano.com/configuration.html#configuring-settings):

```bash
meltano config dbt set project_dir <project_dir>

export DBT_PROJECT_DIR=<project_dir>
```

### Profiles Directory

- Name: `profiles_dir`
- [Environment variable](https://docs.meltano.com/configuration.html#configuring-settings): `DBT_PROFILES_DIR`
- Default: `$MELTANO_PROJECT_ROOT/transform/profile`

The directory where the dbt `profiles.yml` file is stored.

This setting corresponds to [dbt's `--profiles-dir` option](https://docs.getdbt.com/dbt-cli/configure-your-profile#using-a-custom-profile-directory).

#### How to use

Manage this setting using [`meltano config`](https://docs.meltano.com/command-line-interface.html#config) or an [environment variable](https://docs.meltano.com/configuration.html#configuring-settings):

```bash
meltano config dbt set profiles_dir <profiles_dir>

export DBT_PROFILES_DIR=<profiles_dir>
```

### Target

- Name: `target`
- [Environment variable](https://docs.meltano.com/configuration.html#configuring-settings): `DBT_TARGET`
- Default: `$MELTANO_LOAD__DIALECT`, which [will expand to](https://docs.meltano.com/integration.html#pipeline-environment-variables) the value of the [`dialect` extra](https://docs.meltano.com/concepts/plugins#dialect-extra) for the loader used in the pipeline, e.g. `postgres` for `target-postgres` and `snowflake` for `target-snowflake`.

This is the dialect of your warehouse where data is stored. It maps to the [`target:` value](https://github.com/meltano/files-dbt/blob/ca1d0c5395e01a00a8174323301fb94a9910b92a/bundle/transform/profile/profiles.yml#L5) in the dbt [`profiles.yml` file](https://docs.getdbt.com/dbt-cli/configure-your-profile).

#### How to use

This setting is managed by the loader and is not recommended to be changed via the transformer. You can, if needed, overwrite this setting using [`meltano config`](https://docs.meltano.com/command-line-interface.html#config) or an [environment variable](https://docs.meltano.com/configuration.html#configuring-settings):

```bash
meltano config dbt set target <target>

export DBT_TARGET=<target>
```

### Source Schema

- Name: `source_schema`
- [Environment variable](https://docs.meltano.com/configuration.html#configuring-settings): `DBT_SOURCE_SCHEMA`
- Default: `$MELTANO_LOAD__TARGET_SCHEMA`, which [will expand to](https://docs.meltano.com/integration.html#pipeline-environment-variables) the value of the schema setting for the loader used in the pipeline.

This defines the schema were dbt will read data from.

#### How to use

This setting is managed by the loader and is not recommended to be changed via the transformer. You can, if needed, overwrite this setting using [`meltano config`](https://docs.meltano.com/command-line-interface.html#config) or an [environment variable](https://docs.meltano.com/configuration.html#configuring-settings):

```bash
meltano config dbt set source_schema <source_schema>

export DBT_SOURCE_SCHEMA=<source_schema>
```

### Target Schema

- Name: `target_schema`
- [Environment variable](https://docs.meltano.com/configuration.html#configuring-settings): `DBT_TARGET_SCHEMA`
- Default: `analytics`

This is the schema dbt writes transformation results to.

#### How to use

Manage this setting using [`meltano config`](https://docs.meltano.com/command-line-interface.html#config) or an [environment variable](https://docs.meltano.com/configuration.html#configuring-settings):

```bash
meltano config dbt set target_schema <schema>

export DBT_TARGET_SCHEMA=<schema>
```

### Models

- Name: `models`
- [Environment variable](https://docs.meltano.com/configuration.html#configuring-settings): `DBT_MODELS`
- Default: `$MELTANO_TRANSFORM__PACKAGE_NAME $MELTANO_EXTRACTOR_NAMESPACE my_meltano_project`, which [will expand to](https://docs.meltano.com/integration.html#pipeline-environment-variables) the value of the [`package_name` extra](https://docs.meltano.com/concepts/plugins#package-name-extra) for any [transform](https://docs.meltano.com/concepts/plugins#transforms) used in the pipeline, followed by the namespace of the extractor used in the pipeline (e.g. `tap_gitlab` for [`tap-gitlab`](https://meltano.com/plugins/extractors/gitlab.html), followed by `my_meltano_project` (referring to all models local to your dbt project).

This defines the list of models which dbt will run during a transformation.

This setting corresponds to [dbt's `--models` option](https://docs.getdbt.com/reference/commands/run#running-specific-models).

#### How to use

Manage this setting using [`meltano config`](https://docs.meltano.com/command-line-interface.html#config) or an [environment variable](https://docs.meltano.com/configuration.html#configuring-settings):

```bash
meltano config dbt set models <models>

export DBT_MODELS=<models>
```

## Commands

[Meltano commands](https://docs.meltano.com/command-line-interface.html#commands) are shortcuts for combinations of arguments used with [`meltano invoke`](https://docs.meltano.com/command-line-interface.html#invoke). 
The command specified will use the defined arguments and pass along any specified environment variables.
The commands for `dbt` are documented below.

### Clean

- Command: `clean`
- Argument: `clean`
- Reference: [`dbt clean`](https://docs.getdbt.com/reference/commands/clean)

Delete all folders in the `clean-targets` list (usually the `dbt_modules` and `target` directories.)

#### How to use

```bash
meltano invoke dbt:clean
```      

### Compile

- Command: `compile`
- Argument: `compile --models $DBT_MODELS`
- Reference: [`dbt compile`](https://docs.getdbt.com/reference/commands/compile)

Generates executable SQL from source model, test, and analysis files. Compiled SQL files are written to the target/ directory.
View the [Models](#models) documentation for details on the `$DBT_MODELS` environment variable.

#### How to use

```bash
meltano invoke dbt:compile
```            

### Dependencies

- Command: deps
- Argument: `deps`
- Reference: [`dbt deps`](https://docs.getdbt.com/reference/commands/deps)

Pull the most recent version of the dependencies listed in `packages.yml`.

#### How to use

```bash
meltano invoke dbt:deps
```    

### Run

- Command: `run`
- Argument: `run --models $DBT_MODELS`
- Reference: [`dbt run`](https://docs.getdbt.com/reference/commands/run)

Compile SQL and execute against the current target database. 
View the [Models](#models) documentation for details on the `$DBT_MODELS` environment variable.

#### How to use

```bash
meltano invoke dbt:run
```    

### Seed

- Command: `seed`
- Argument: `seed`
- Reference: [`dbt seed`](https://docs.getdbt.com/reference/commands/seed)

Load data from csv files into your data warehouse.

#### How to use

```bash
meltano invoke dbt:seed
```   

### Snapshot

- Command: `snapshot`
- Argument: `snapshot`
- Reference: [`dbt snapshot`](https://docs.getdbt.com/reference/commands/snapshot)

Execute snapshots defined in your project.

#### How to use

```bash
meltano invoke dbt:snapshot
```   

### Test

- Command: `test`
- Argument: `test`
- Reference: [`dbt test`](https://docs.getdbt.com/reference/commands/test)

Runs tests on data in deployed models.

#### How to use

```bash
meltano invoke dbt:test
```

## Troubleshooting

### No Models Running

If no models are running, consider overriding the [`models` setting](#models) using a [pipeline-specific configuration](https://docs.meltano.com/integration.html#pipeline-specific-configuration). 

You can also add a [custom](https://docs.meltano.com/configuration.html#custom-settings) [extra](https://docs.meltano.com/configuration.html#plugin-extras) to your extractor definition in your [`meltano.yml` project file](https://docs.meltano.com/concepts/project#meltano-yml-project-file), that can then be [referenced](https://docs.meltano.com/integration.html#pipeline-environment-variables) from `dbt`'s `models` setting using an [environment variable](https://docs.meltano.com/configuration.html#expansion-in-setting-values):

```bash
# meltano.yml
plugins:
  extractors:
  - name: tap-foo
    model_name: my_dbt_models # Specify any models here
# ...
  transformers:
  - name: dbt
    config:
      models: $MELTANO_EXTRACT__MODEL_NAME # Refers to the extractor's `model_name`
```
