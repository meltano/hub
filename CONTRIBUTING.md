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

## Adding or Updating Plugins

### Quick Start

To add a new plugin or variant of an existing one, run the following command and provide any input that it prompts for:

```bash
hub-utils add
```

To update an existing variant, run the following command and provide any input that it prompts for:

```bash
hub-utils update-definition
```

### Step-by-Step Guide: Adding a New Plugin

This comprehensive guide walks you through adding a new plugin to MeltanoHub using the `hub-utils add` command.

#### Prerequisites

1. **Clone the Hub repository** (if you haven't already):

   ```bash
   git clone https://github.com/meltano/hub.git
   cd hub
   ```

2. **Install hub-utils**:

   ```bash
   # For development (if working from hub repo with hub-utils as subdirectory)
   cd hub-utils
   uv sync
   cd ..

   # Or using pipx (for standalone installation)
   pipx install git+https://github.com/meltano/hub-utils.git
   ```

3. **Ensure you're in the hub repository root**:

   ```bash
   cd /path/to/hub
   ```

   Or set the `HUB_ROOT_PATH` environment variable if running from elsewhere:

   ```bash
   export HUB_ROOT_PATH='/path/to/hub'
   ```

#### Basic Usage

Run the command from the hub repository root:

```bash
# Interactive mode (will prompt for repo URL)
uv run hub-utils add

# Or provide the repo URL directly
uv run hub-utils add --repo-url https://github.com/username/tap-example
```

#### What the Command Does

The `add` command automates the entire plugin addition workflow:

1. **Collects plugin information**: Prompts for plugin name, type (extractor/loader), pip URL, namespace, and executable
2. **Detects SDK-based plugins**: Automatically identifies if the plugin uses Meltano SDK
3. **Extracts metadata automatically**: For SDK-based plugins, it:
   - Creates a temporary Python environment
   - Installs the plugin using pip
   - Runs `<plugin> --about` to extract settings, capabilities, and configuration
   - Parses the JSON output to generate the plugin definition
4. **Creates plugin definition**: Generates a YAML file at `_data/meltano/{plugin_type}/{plugin_name}/{variant}.yml`
5. **Updates default variants**: Adds an entry to `_data/default_variants.yml` for new plugins
6. **Manages maintainer info**: Updates `_data/maintainers.yml` with variant maintainer information
7. **Handles logos**: Prompts for logo upload or attempts automatic download (for Hotglue variants)
8. **Formats YAML files**: Runs yamllint to ensure consistent formatting

#### Complete Example Workflow

Here's a complete example of adding a new SDK-based tap:

```bash
# 1. Navigate to hub repository
cd /path/to/hub

# 2. Create a new branch
git checkout -b add-tap-example

# 3. Run the add command with repo URL
uv run hub-utils add --repo-url https://github.com/meltanolabs/tap-slack

# 4. The command will prompt for information (with smart defaults):
# plugin name [tap-slack]: <press enter to accept>
# plugin type [extractors]: <press enter to accept>
# pip_url [git+https://github.com/meltanolabs/tap-slack.git]: <press enter to accept>
# namespace [tap_slack]: <press enter to accept>
# executable [tap-slack]: <press enter to accept>
# is_meltano_sdk [True]: <press enter to accept>

# 5. For SDK-based plugins, it will automatically:
#    - Create a temporary virtual environment
#    - Install the plugin: pip install git+https://github.com/meltanolabs/tap-slack.git
#    - Run: tap-slack --about --format json
#    - Parse settings, capabilities, and configuration from the output

# 6. The command will prompt for:
# keywords [['meltano_sdk']]: <press enter to accept>
# plugin variant [meltanolabs]: <press enter to accept>

# 7. Output confirms creation:
# _data/meltano/extractors/tap-slack/meltanolabs.yml
# Adds extractors tap-slack (meltanolabs)

# 8. Review the generated file
cat _data/meltano/extractors/tap-slack/meltanolabs.yml

# 9. Test the hub site locally
gridsome develop
# Visit http://localhost:8080 and navigate to your plugin

# 10. Commit and push
git add .
git commit -m "Add tap-slack (meltanolabs variant)"
git push origin add-tap-example

# 11. Open a pull request on GitHub
```

#### Command Options

**Provide repo URL directly**:

```bash
uv run hub-utils add --repo-url https://github.com/username/tap-example
```

**Auto-accept mode** (skip all prompts and use defaults):

```bash
uv run hub-utils add --repo-url https://github.com/username/tap-example --auto-accept
```

**Specify Python version** (useful if the plugin requires a specific Python version):

```bash
uv run hub-utils add --repo-url https://github.com/username/tap-example --python python3.11
```

#### Special Cases

**Airbyte Connectors**

The command automatically detects Airbyte connector repositories:

```bash
uv run hub-utils add --repo-url https://github.com/airbytehq/airbyte/tree/master/source-example
# Will prompt: "Is this an Airbyte variant?" [Y/n]
```

If confirmed, it will use the Airbyte wrapper and extract metadata from the Airbyte connector specification.

**Hotglue Variants**

For Hotglue plugins, the command attempts to download logos automatically from Hotglue's CDN:

```bash
uv run hub-utils add --repo-url https://github.com/hotgluexyz/tap-salesforce
# Will prompt: "Is this a Hotglue variant?" [Y/n]
# Automatically downloads logo from: https://s3.amazonaws.com/cdn.hotglue.xyz/images/logos/{service_name}.{ext}
```

**Non-SDK Plugins**

If a plugin is not SDK-based or if automatic metadata extraction fails, the command will enter interactive mode and prompt for each setting individually:

```bash
# After determining the plugin is not SDK-based:
# The command will help you build settings one at a time
# setting name: api_key
# setting label [API Key]:
# setting description: Your API key for authentication
# setting kind (string/boolean/integer/object/array) [string]:
# setting required [True]:
```

#### YAML Linting

If you make manual changes to the YAML files, ensure they pass linting before creating a PR:

```bash
# Automatically fix any lint violations
uv run hub-utils yamllint fix _data/meltano/extractors/tap-example/username.yml

# Check for lint violations (without fixing)
uv run hub-utils yamllint lint _data/meltano/extractors/tap-example/username.yml
```

#### Troubleshooting

**Plugin installation fails**

Try specifying a different Python version:

```bash
uv run hub-utils add --repo-url https://github.com/username/tap-example --python python3.9
```

**SDK metadata extraction fails**

The command will automatically fall back to manual entry mode. You'll be prompted to enter settings one by one. You can also manually inspect the plugin's documentation and update the YAML file afterward.

**Generated YAML has validation errors**

Run yamllint to fix formatting issues:

```bash
uv run hub-utils yamllint fix _data/meltano/extractors/tap-example/username.yml
```

**Need to update an existing plugin**

Use `update-definition` instead of `add`:

```bash
uv run hub-utils update-definition --repo-url https://github.com/username/tap-example
```

**Command doesn't recognize the hub repository**

Set the `HUB_ROOT_PATH` environment variable:

```bash
export HUB_ROOT_PATH='/path/to/hub'
uv run hub-utils add --repo-url https://github.com/username/tap-example
```

#### What Gets Created

After running `hub-utils add`, the following files are created or modified:

1. **Plugin definition YAML**: `_data/meltano/{extractors|loaders}/{plugin-name}/{variant}.yml`

   - Contains all plugin metadata, settings, and capabilities

2. **Default variants file**: `_data/default_variants.yml`

   - Updated with an entry for new plugins (not existing variants)

3. **Maintainers file**: `_data/maintainers.yml`

   - Updated with maintainer information for the variant

4. **Logo file** (optional): `static/assets/logos/{extractors|loaders}/{plugin-name}.{svg|png}`
   - Added if you provide a logo or if automatically downloaded (Hotglue variants)

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
