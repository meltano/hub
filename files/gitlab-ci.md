---
title: GitLab CI
layout: plugin_page
description: GitLab CI file bundle with configuration to manage CICD using GitLab
---

The [`gitlab-ci`](https://docs.gitlab.com/ee/ci/) [file bundle](https://docs.meltano.com/concepts/plugins#file-bundles) installs files into your Meltano project to accelerate onboarding and integrating the plugin into your project.
This file bundle installs GitLab CI configuration files used as a starting place for your CICD pipelines.

- **Repository**: <https://github.com/meltano/files-gitlab-ci>
- **Documentation**: <https://docs.gitlab.com/ee/ci/>
- **Maintainer**: Meltano community
- **Maintenance status**: Active

## Getting Started

### Prerequisites

If you haven't already, follow the [Getting Started guide](https://docs.meltano.com/getting-started.html):

1. [Install Meltano](https://docs.meltano.com/getting-started.html#install-meltano)
1. [Create your Meltano project](https://docs.meltano.com/getting-started.html#create-your-meltano-project)

### Installation and configuration

1. Add the `gitlab-ci` file bundle to your project using [`meltano add`](https://docs.meltano.com/command-line-interface.html#add):

    ```bash
    meltano add files gitlab-ci
    ```

### Next steps

1. Make any customizations to your `.gitlab-ci.yml` files to execute any build, test, deploy, etc. steps needed for your project.

If you run into any issues, chat with us in [#troubleshooting](https://meltano.slack.com/archives/C01TCRBBJD7) on [Slack](https://meltano.com/slack).
