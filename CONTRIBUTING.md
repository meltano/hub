# Contributing to the Hub Website

_This page is about contributing to the Hub website. For information about contributing plugins to the Hub, please reference the plugins contribution page._

Let's build together! Please see our [Contributor Guide](https://docs.meltano.com/contribute/)
for more information on contributing to Meltano.

We believe that everyone can contribute and we welcome all contributions.
If you're not sure what to work on, here are some [ideas to get you started](https://github.com/meltano/meltano/issues?q=is%3Aissue+is%3Aopen+label%3A%22accepting+merge+requests%22+).

Chat with us in [#contributing](https://meltano.slack.com/archives/C013Z450LCD) on [Slack](https://meltano.com/slack).

Contributors are expected to follow our [Code of Conduct](https://docs.meltano.com/contribute/#code-of-conduct).

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

### Linters

You can use `pre-commit` to run the linters before committing.

```console
pipx install pre-commit
pre-commit install
```

This will run the linters on all files that are staged for commit. Included linters:

- [yamlllint](https://yamllint.readthedocs.io/en/stable/)

Theres a utility script that makes a best effort to help reformat yaml files to conform to the
yamllint rules.
To use the script run:

```bash
# Run on a single file
poetry run python utility_scripts/plugin_definitions/yaml_lint_fix.py _data/meltano/extractors/tap-3plcentral/bytecodeio.yml

# Run on all .yml files in the `_data/` directory including subdirectories
poetry run python utility_scripts/plugin_definitions/yaml_lint_fix.py
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
