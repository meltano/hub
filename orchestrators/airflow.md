---
title: Airflow
layout: plugin_page
description: Use Meltano to orchestrate and schedule your data pipelines using Airflow.
---

The [`Airflow`](https://airflow.apache.org/) [orchestrator](https://docs.meltano.com/concepts/plugins#orchestrators) allows for workflows to be programmatically authored, scheduled, and monitored.

- **Repository**: <https://github.com/apache/airflow/>
- **Documentation**: <https://airflow.apache.org/docs/>
- **Maintainer**: [Apache Foundation](https://www.apache.org/)
- **Maintenance status**: Active

## Getting Started

### Prerequisites

If you haven't already, follow the [Getting Started guide](https://docs.meltano.com/getting-started.html):

1. [Install Meltano](https://docs.meltano.com/getting-started.html#install-meltano)
1. [Create your Meltano project](https://docs.meltano.com/getting-started.html#create-your-meltano-project)

### Installation and configuration

1. Add the `Airflow` orchestrator to your project using [`meltano add`](https://docs.meltano.com/command-line-interface.html#add):

    ```bash
    meltano add orchestrator airflow
    ```

1. Configure the [settings](#settings) below using [`meltano config`](https://docs.meltano.com/command-line-interface.html#config).

### Next steps

1. Use the [`meltano schedule`](https://docs.meltano.com/reference/command-line-interface#schedule) command to create pipeline schedules in your project, to be run by Airflow.
1. Start Scheduler and Webserver or execute Airflow commands directly using the instructions in [the Meltano docs](https://docs.meltano.com/guide/orchestration#starting-the-airflow-scheduler).

If you run into any issues, chat with us in [#troubleshooting](https://meltano.slack.com/archives/C01TCRBBJD7) on [Slack](https://meltano.com/slack).
