---
title: Airflow
layout: plugin_page
description: Airflow file bundle
---

The [`airflow`](https://airflow.apache.org/) [file bundle](https://docs.meltano.com/concepts/plugins#file-bundles) installs files into your Meltano project to accelerate onboarding and integrating the plugin into your project.
This file bundle installs a DAG generator that works together with Meltano schedules to auto generate Airflow DAGs based on Meltano configurations.

- **Repository**: <https://github.com/meltano/files-airflow>
- **Documentation**: <https://airflow.apache.org/docs/>
- **Maintainer**: Meltano community
- **Maintenance status**: Active

## Getting Started

### Prerequisites

If you haven't already, follow the [Getting Started guide](https://docs.meltano.com/getting-started.html):

1. [Install Meltano](https://docs.meltano.com/getting-started.html#install-meltano)
1. [Create your Meltano project](https://docs.meltano.com/getting-started.html#create-your-meltano-project)

### Installation and configuration

1. Add the `airflow` file bundle to your project using [`meltano add`](https://docs.meltano.com/command-line-interface.html#add):

    ```bash
    meltano add files airflow
    ```

### Next steps

1. Optionally customize the DAG generator or simply create Meltano pipelines [`schedules`](https://docs.meltano.com/reference/command-line-interface#schedule) and start your Airflow instance.

If you run into any issues, chat with us in [#troubleshooting](https://meltano.slack.com/archives/C01TCRBBJD7) on [Slack](https://meltano.com/slack).
