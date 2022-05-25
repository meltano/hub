---
title: dbt-snowflake - data build tool
layout: plugin_page
description: dbt file bundle for Snowflake
---

The [`dbt-snowflake`](https://www.getdbt.com) [file bundle](https://docs.meltano.com/concepts/plugins#file-bundles) for Snowflake installs files into your Meltano project to accelerate onboarding and integrating the plugin into your project.
This file bundle installs your dbt project directory including configuration files like `dbt_projects.yml` and `profiles.yml` with defaults in place to allow you to connect to you warehouse easily.

- **Repository**: <https://gitlab.com/meltano/files-dbt-snowflake>
- **Documentation**: <https://docs.getdbt.com/>
- **Maintainer**: Meltano community
- **Maintenance status**: Active

## Getting Started

### Prerequisites

If you haven't already, follow the [Getting Started guide](https://docs.meltano.com/getting-started.html):

1. [Install Meltano](https://docs.meltano.com/getting-started.html#install-meltano)
1. [Create your Meltano project](https://docs.meltano.com/getting-started.html#create-your-meltano-project)

### Installation and configuration

1. Add the `dbt-snowflake` file bundle to your project using [`meltano add`](https://docs.meltano.com/command-line-interface.html#add):

    ```bash
    meltano add files dbt-snowflake
    ```

1. Configure the [settings](#settings) below using [`meltano config`](https://docs.meltano.com/command-line-interface.html#config).

### Next steps

1. [Transform loaded data for analysis](https://docs.meltano.com/getting-started.html#transform-loaded-data-for-analysis)

If you run into any issues, chat with us in [#troubleshooting](https://meltano.slack.com/archives/C01TCRBBJD7) on [Slack](https://meltano.com/slack).
