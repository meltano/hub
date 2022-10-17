# hub-utils

poetry install
poetry run hub_utils --help

poetry run hub_utils add https://github.com/birdiecare/tap-cqc-org-uk
poetry run hub_utils add https://github.com/birdiecare/tap-cqc-org-uk --auto-accept

- evaluate
    - validate against minimum requirements (settings, etc.)
    - sdk
    - commits
    - last update
    - usage
    - 
- add
  - given a repo_url, pull SDK metadata if it exists, ask for user input as needed
  - prompt for alternative naming, if its meltano-xyz and just fits under an existing xyz plugin dir
  - write definition file
  - add as default variant if the only one
  - add to maintainers if not exists
  - prompt for a logo url path
- add_bulk
  - same as add but uses a CSV as input
- update - given a repo_url, check for updates
- delete - check for repos that dont exist and remove

- labels
- name + file check
- maintainer exists
- state capabilities


Ideas:
- it should help with settings too
- request all setting names at once, to get them all stored, then ask about updates to defaults and descriptions one by one
- auto create label, default to string, description as label
- 