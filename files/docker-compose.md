---
title: Docker Compose
layout: plugin_page
description: Docker compose file bundle running your Meltano project
---

The [`docker-compose`](https://docs.docker.com/compose/) [file bundle](https://docs.meltano.com/concepts/plugins#file-bundles) installs files into your Meltano project to accelerate onboarding and integrating the plugin into your project.
This file bundle installs docker-compose files used for spinning up your Meltano project service using docker containers.


- **Repository**: <https://github.com/meltano/files-docker-compose>
- **Documentation**: <https://docs.docker.com/compose/>
- **Maintainer**: Meltano community
- **Maintenance status**: Active

## Getting Started

### Prerequisites

If you haven't already, follow the [Getting Started guide](https://docs.meltano.com/getting-started.html):

1. [Install Meltano](https://docs.meltano.com/getting-started.html#install-meltano)
1. [Create your Meltano project](https://docs.meltano.com/getting-started.html#create-your-meltano-project)

### Installation and configuration

1. Add the `docker-compose` file bundle to your project using [`meltano add`](https://docs.meltano.com/command-line-interface.html#add):

    ```bash
    meltano add files docker-compose
    ```

### Next steps

1. Follow the advanced instructions to uncomment the services you want to run and spin them up using [`docker-compose up -d`](https://github.com/meltano/files-docker-compose/blob/main/bundle/README.md)

If you run into any issues, chat with us in [#troubleshooting](https://meltano.slack.com/archives/C01TCRBBJD7) on [Slack](https://meltano.com/slack).
