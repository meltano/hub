<!---
Use this template when adding a new Singer tap or target to the hub. 
--->


All Singer definitions are stored in `/_data/taps/` or `/_data/targets`. The minimial requirement for adding a tap or target will match the following format:



## Checklist

- [ ] Add a file in the appropriate folder (`/taps` or `/targets`). The name of the file should match the name of the tap. If there is already one, add a descriptor to the name such as `-search`.
   - [ ] Attempting to create the file directly should automatically fork the repo and prompt you to create a new branch. You can name the branch anything you like, for instance `tap-mynewsource`.
- [ ] If you've not already done so, create a Merge Request from the new branch and select the template "Add a New Singer Connector".
- [ ] Add a png logo image in `/assets/<taps/targets>`. The image name must match the YAML file name and should be a reasonable size (ideally less than 100K).
- [ ] Tag `@tayloramurphy` or `@aaronsteers` to flag it for review. Or post to the hub channel on Meltano slack.


## Sample yaml file

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
  name: Name of the GitHub/GitLab namespace
  pip_url: git+<git_url>.git or pip instal name
  repo: repo URL
  settings:
    # Describe the list of supported settings, for example:
    - name: project_ids
      kind: array
      description: Array of project IDs.
    - name: username
      kind: string
      description: Credentials used when for connecting to the source.
    - name: password
      kind: password
      description: Credentials used when for connecting to the source.
```

