---
title: SQLFluff
layout: plugin_page
description: SQLFluff utility
---

The [`sqlfluff`](https://github.com/sqlfluff/sqlfluff) [utility](https://docs.meltano.com/concepts/plugins#utilities) is a linting tool for SQL files, often used with dbt to enforce SQL code standards.

- **Repository**: <https://github.com/sqlfluff/sqlfluff>
- **Documentation**: <https://docs.sqlfluff.com>
- **Maintainer**: [SQLFluff community](https://www.sqlfluff.com/)
- **Maintenance status**: Active

## Getting Started

### Prerequisites

If you haven't already, follow the [Getting Started guide](https://docs.meltano.com/getting-started.html):

1. [Install Meltano](https://docs.meltano.com/getting-started.html#install-meltano)
1. [Create your Meltano project](https://docs.meltano.com/getting-started.html#create-your-meltano-project)

### Installation and configuration

1. Add the `sqlfluff` utility to your project using [`meltano add`](https://docs.meltano.com/command-line-interface.html#add):

    ```bash
    meltano add utility sqlfluff
    ```

1. Configure the [settings](#settings) below using [`meltano config`](https://docs.meltano.com/command-line-interface.html#config).

### Next steps

1. Refer to [the installation instructions](https://docs.meltano.com/concepts/plugins#sqlfluff) for advanced configurations.
1. Customize [the config files](https://docs.sqlfluff.com/en/stable/configuration.html) to match your team's style guide.
1. Run `meltano run sqlfluff:lint` to lint your SQL files.

If you run into any issues, chat with us in [#troubleshooting](https://meltano.slack.com/archives/C01TCRBBJD7) on [Slack](https://meltano.com/slack).
