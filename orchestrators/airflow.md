---
title: airflow
layout: plugin_page
description: something about airflow
---

The [`airflow`](https://airflow.apache.org/) [orchestrator](https://docs.meltano.com/orchestration.html) allows for workflows to be programmatically authored, scheduled, and monitored.

- **Repository**: <https://github.com/apache/airflow/>
- **Documentation**: <https://airflow.apache.org/docs/>
- **Maintainer**: ???
- **Maintenance status**: Active

## Getting Started

### Prerequisites

If you haven't already, follow the [Getting Started guide](https://docs.meltano.com/getting-started.html):

1. [Install Meltano](https://docs.meltano.com/getting-started.html#install-meltano)
1. [Create your Meltano project](https://docs.meltano.com/getting-started.html#create-your-meltano-project)
1. Load data into your warehouse by following the rest of the [Getting Started guide](https://docs.meltano.com/getting-started.html).

### Installation and configuration

1. Add the `airflow` orchestrator to your project using [`meltano add`](https://docs.meltano.com/command-line-interface.html#add):

    ```bash
    meltano add orchestrator airflow
    ```

1. Configure the [settings](#settings) below using [`meltano config`](https://docs.meltano.com/command-line-interface.html#config).

### Next steps

1. ???

If you run into any issues, [learn how to get help](https://docs.meltano.com/getting-help.html).
