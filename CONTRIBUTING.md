# Contributing to the Hub Website

_This page is about contributing to the Hub website. For information about contributing plugins to the Hub, please reference the plugins contribution page._

Let's build together! Please see our [Contributor Guide](https://docs.meltano.com/contribute/)
for more information on contributing to Meltano.

We believe that everyone can contribute and we welcome all contributions.
If you're not sure what to work on, here are some [ideas to get you started](https://github.com/meltano/hub/issues?q=is%3Aissue+is%3Aopen+label%3A%22Accepting+Pull+Requests%22)
  
Chat with us in [#contributing](https://meltano.slack.com/archives/C013Z450LCD) on [Slack](https://meltano.com/slack).

Contributors are expected to follow our [Code of Conduct](https://docs.meltano.com/contribute/#code-of-conduct).


## hub-utils CLI

MeltanoHub has some conventions and patterns that need to be followed in order for the plugin pages to render properly and CI tests to pass.
This can sometimes make it difficult for our team and community members to contribute changes.
To help with this we created a [hub-utils CLI](https://github.com/meltano/hub-utils) that offers an interactive CLI interface for common operations.
For example it will help you add or update plugins, along the way it will prompt for information it needs to fulfil the plugin definition and if the plugin is SDK based it will scrape most of the information for you so you don't need to provide it.
It does it's best to default to the correct answers and fill common descriptions (i.e. start_date) and labels for you.


This assumes you already have pipx installed, see the meltano [install-pipx docs](https://docs.meltano.com/guide/installation-guide#install-pipx) for details.

```bash
pipx install git+https://github.com/meltano/hub-utils.git
```

The CLI assumes your terminal is in the root of the hub repository, if you need to run it outside the hub repository root you can set the path using the `HUB_ROOT_PATH` environment variable.

## Add or Updating Plugins

To add a new plugin or variant of an existing one, run the following command and provide any input that it prompts for.

```bash
hub-utils add
```

To update an existing variant, run the following command and provide any input that it prompts for.

```bash
hub-utils update-definition
```

If you chose to make any manual changes to the yaml files, make sure you run the yaml linters to fix any linting violations before creating a PR.

```bash
# Automatically attempt to fix any lint violations
hub-utils yamllint fix _data/meltano/extractors/tap-3plcentral/bytecodeio.yml

# Check for lint violations
hub-utils yamllint lint _data/meltano/extractors/tap-3plcentral/bytecodeio.yml
```

## Automated plugin testing

Repo maintainers with `write` access are able to perform automated plugin testing using slash commands in any issue or pull request.

In any issue or pull request, type the following on the first line of a new comment:

```txt
/test-plugin name=PLUGIN_NAME [pip-url=PIP_URL]
```

If `pip-url` is omitted, the `name` field will be used as `pip-url`.

For more information about slash commands and slash command dispatch:

- https://github.com/peter-evans/slash-command-dispatch

## Installing prereqs

```console
yarn
yarn add --global @gridsome/cli
```

## Build and serve the project

Build for development and get live updates as files are changed:

```console
# Update packages if needed:
yarn

# Build the site in live-update mode:
gridsome develop
```

## Tailwind Dev Configuration

During development, the hot-reload dev server doesn't quite play nice with tailwind. To avoid having to restart it constantly, there's a workaround inside `tailwind.config.js` that you can uncomment.

## Adding and managing content pages in markdown

Markdown content pages may be added under `./static/markdown`.

For example:

- `./static/markdown/singer-docs.md`
- `./static/markdown/singer-spec.md`

Any `.md` files loaded to this directory will be imported into the GraphQL data model and transformed into HTML.

Markdown files can have front-matter as in the following, which will be rendered into the GraphQL data model:

```txt
---
title: "Singer Docs"
description: "The docs page for Singer"
---

# Singer Docs

This is a `test`.
```

Pages will be make available at their path relative to the `/static/markdown` folder. For example, the file `/src/static/markdown/singer/docs.md` will be rendered at `hub.meltano.com/singer/docs/`.

Markdown pages are rendered using the `MarkdownDocs` template, using `/src/templates/MarkdownDocs.vue`.

### GraphQL query for markdown docs

To better understand the data model for markdown data files, use the following query at the GraphQL endpoint (usually [http://localhost:8080/\_\_explore](http://localhost:8080/___explore)):

```graphql
query MarkdownDocs {
  markdownDocs: allMarkdownDocs {
    edges {
      node {
        id
        path
        description
        title
        content
        fileInfo {
          directory
          extension
          path
          name
        }
      }
    }
  }
}
```
