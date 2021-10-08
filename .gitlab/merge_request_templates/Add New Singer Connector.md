<!---
Use this template when adding a new Singer tap or target to the hub. 
--->


All Singer definitions are stored in `/_data/taps/` or `/_data/targets`. The minimial requirement for adding a tap or target will match the following format:

```yaml
description: General description of what the company behind the API does
domain:
  description: Cloud-based Warehouse Management System (WMS)
  name: Name of the API e.g. Marketo API
  type: Review the JSON Schema for latest options. Currently api, file, database.
  url: URL of the developer documentation or website
label: Properly formatted label of the connector
name: The unique name of the connector
singer_name: The Singer specific name of the connector. Typically tap-<name> or target-<name>
type: tap or target
variants: # an array of variant types
- default: true or false
  maintenance_status: "Options: Active, Unresponsive, Unknown"
  meltano_sdk: true or false
  name: Name of the GitHub/GitLab namespace
  pip_url: git+<git_url>.git or pip instal name
  repo: repo URL
  capabilities:
    - catalog
    - discover
  settings: [] # Can be an empty array if unknown
```


## Checklist

- [ ] Add a file in the appropriate folder (/taps or /targets). The name of the file should match the name of the tap. If there is already one, add a descriptor to the name such as `-search`.
- [ ] Add a png logo image in `/assets/<taps or targets>`. The image name must match the YAML file name.
- [ ] Tag `@tayloramurphy` or `@pnadolny13` to flag it for review. Or post to the hub channel on Meltano slack.

## Reviewer Checklist

- [ ] Validate file against JSON Schema. https://www.jsonschema.net/home is an option.
- [ ] Build website locally and validate everything works.

