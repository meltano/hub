<!---
Use this template when adding a new Singer tap or target to the hub.
--->


All Singer definitions are stored in `/_data/taps/` or `/_data/targets` and logo images are in `/assets/logos/<taps or targets>`. The minimal steps for adding a tap or target are the following:

Reference "How to Submit a Singer Connector to MeltanoHub" [YouTube video](https://www.youtube.com/watch?v=hKbHB3LHbEA).

## Checklist

- [ ] Fork the MeltanoHub and create a branch, you can name the branch anything you like.
- [ ] Add a yaml configuration file in the appropriate folder (`/_data/taps/` or `/_data/targets`). The name of the file should match the name of the tap. If there is already one, add a descriptor to the name such as `-search`.
- [ ] Add a png logo image in `/assets/logos/<taps or targets>`. The image name must match the YAML file name and should be a reasonable size (ideally less than 100K).
- [ ] Create a Merge Request to `main` from the new branch in your fork and select the template "Add a New Singer Connector".
- [ ] Tag `@tayloramurphy` or `@pnadolny13` to flag it for review. Or post to the hub channel on Meltano slack.

## Detailed Steps (Git Web Editor)

- Click Web IDE on the [MeltanoHub repo](https://github.com/meltano/hub)
- You'll be prompted to create a fork since you dont have access to edit directly. This automatically create a fork in your project and land you in the web editor.
- Add your yaml config file in `/_data/meltano/extractors` by clicking "New File". You can use the sample below to get started.
- Upload your png image in `/assets/logos/<extractors or loaders>` by clicking "Upload File".
- Click the commit, write a write a message, then commit again (keep "Create new branch" and "Start a new merge request selected")
- Choose the "Add new Singer Connector" template in the merge request
- Tag `@tayloramurphy` or `@pnadolny13`

## Sample yaml file

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
  pip_url: git+<git_url>.git or pip install name
  repo: repo URL
  capabilities:
    # Chose the capabilities that the connector supports
    # Checkout for a list and details - https://hub.meltano.com/singer/docs#singer-connector-capabilities
    # Tap Capability Options
    - about
    - activate-version
    - batch
    - stream-maps
    - schema-flattening
    - catalog
    - properties
    - discover
    - state
    - test
    - log-based
    # Target Capability Options
    - about
    - activate-version
    - batch
    - stream-maps
    - schema-flattening
    - soft-delete
    - hard-delete
    - datatype-failsafe
    - record-flattening
  settings:
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

