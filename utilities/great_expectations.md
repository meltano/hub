---
title: Great Expectations
layout: plugin_page
description: Great Expectations utility
---

The [`great-expectations`](https://github.com/great-expectations/great_expectations) [utility](https://docs.meltano.com/concepts/plugins#utilities) helps data teams eliminate pipeline debt, through data testing, documentation, and profiling.

- **Repository**: <https://github.com/great-expectations/great_expectations>
- **Documentation**: <https://docs.greatexpectations.io/docs/>
- **Maintainer**: [Great Expectations](https://greatexpectations.io/)
- **Maintenance status**: Active

## Getting Started

### Prerequisites

If you haven't already, follow the [Getting Started guide](https://docs.meltano.com/getting-started.html):

1. [Install Meltano](https://docs.meltano.com/getting-started.html#install-meltano)
1. [Create your Meltano project](https://docs.meltano.com/getting-started.html#create-your-meltano-project)

### Installation and configuration

1. Add the `great-expectations` utility to your project using [`meltano add`](https://docs.meltano.com/command-line-interface.html#add):

    ```bash
    meltano add utility great_expectations
    ```

1. Configure the [settings](#settings) below using [`meltano config`](https://docs.meltano.com/command-line-interface.html#config).

### Next steps

1. Refer to [the installation instructions](https://docs.meltano.com/concepts/plugins#great-expectations) for advanced configurations.
1. Create expectations suites and checkpoints!

If you run into any issues, chat with us in [#troubleshooting](https://meltano.slack.com/archives/C01TCRBBJD7) on [Slack](https://meltano.com/slack).
