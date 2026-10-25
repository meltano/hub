# AGENTS.md

MeltanoHub: a catalog of Meltano plugins (extractors, loaders, utilities, etc.), published at https://hub.meltano.com/.

## Layout

- `_data/meltano/<type>/<plugin-name>/<variant>.yml`: one file per plugin variant. The file name is the variant name (usually the GitHub owner of the repo). `<type>` is `extractors`, `loaders`, `utilities`, ...
- `_data/default_variants.yml`: maps each plugin name to its default variant. Keep it sorted.
- `_data/maintainers.yml`: variant owners.
- `_data/variant_metrics.yml`, `singer/`: generated. Don't edit by hand.
- `schemas/`: JSON schemas that plugin definitions must satisfy.
- `hub-utils/`: Python CLI used to add, refresh and lint plugin definitions.
- `src/`, `gridsome.*`: the Gridsome (Vue) website.

## Working with `hub-utils`

Run from the repo root:

```bash
uv sync
uv run hub-utils --help
uv run hub-utils add --repo-url <repo-url> [--auto-accept]
uv run hub-utils yamllint lint   # or `fix`
cd hub-utils && uv run pytest
```

## Conventions

- Plugin definition files are YAML linted with `yamllint` (`.yamllint.yaml`); run `hub-utils yamllint fix` rather than reformatting by hand.
- When renaming a variant, update all of: the file name, the `variant:` field, `repo` and `pip_url`, and the `_data/default_variants.yml` entry.
- Commands such as `hub-utils add` may leave stray files in the repo root; delete them before committing.
- Use conventional-commit style messages (`feat:`, `fix:`, `chore:`).
