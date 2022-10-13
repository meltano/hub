All Singer definitions are stored in `/_data/taps/` or `/_data/targets`. The minimal requirement for adding a tap or target will match the following format:

```yaml
description: General description of what the company behind the API does
entity_type: Review the JSON Schema for latest options. Currently api, file, database.
entity_url: URL of the developer documentation or website
label: Properly formatted label of the connector
name: The unique name of the connector
singer_name: The Singer specific name of the connector. Typically tap-<name> or target-<name>
type: tap or target
variants: # an array of variant types
- default: true or false
  maintenance_status: "Options: active, beta, development, inactive, unknown"
  meltano_sdk: true or false
  name: Name of the GitHub/GitLab namespace
  pip_url: git+<git_url>.git or pip instal name
  repo: repo URL
  capabilities:
    - catalog
    - discover
  settings:
    # Can be an empty array if unknown: []
    # Describe the list of supported settings, for example:
    - name: project_ids
      kind: array
      label: Project IDs
      description: Array of project IDs.
    - name: username
      label: Username
      description: Credentials used when for connecting to the source.
    - name: password
      kind: password
      label: Password
      description: Credentials used when for connecting to the source.
```

## Checklist

- [ ] Add/update the file in the appropriate folder (`/taps` or `/targets`). The name of the file should match the name of the tap. If there is already one, add a descriptor to the name such as `-search`.
- [ ] Add/update the PNG logo image in `/assets/logos/<taps or targets>`. The image name must match the YAML file name.
- [ ] Tag `@tayloramurphy` or `@pnadolny13` to flag it for review. Or post to the [#hub](https://meltano.slack.com/archives/C01UGBSJNG5) channel on Meltano slack.

## Reviewer Checklist

- [ ] Validate file against JSON Schema. https://www.jsonschema.net/home is an option.
- [ ] Build website locally and validate everything works.
