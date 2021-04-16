---
name: CSV
type: target
target_type: file
singer_name: target-csv
description: Singer target for loading data into [Comma Separated Values (CSV)](https://en.wikipedia.org/wiki/Comma-separated_values) files
repo: https://github.com/singer-io/target-csv
repo_forks: https://github.com/singer-io/target-csv/network
pip_url: target-csv
maintainer: 
  name: Stitch
  link: https://www.stitchdata.com/
maintenance_status: Unresponsive
adoptable: true
dialect: csv
settings:
  - name: destination_path
    description: Sets the destination path the CSV files are written to, relative to the project root. The directory needs to exist already, it will not be created automatically. To write CSV files to the project root, set an empty string (`""`).
    value: output
  - name: delimiter
    kind: options
    options:
      - label: Comma (,)
        value: ','
      - label: Tab (  )
        value: '\t'
      - label: Semi-colon (;)
        value: ';'
      - label: Pipe (|)
        value: '|'
    value: ','
    description: A one-character string used to separate fields. It defaults to a comma (,).
  - name: quotechar
    kind: options
    options:
      - label: Single Quote (')
        value: "'"
      - label: Double Quote (")
        value: '"'
    value: "'"
    description: A one-character string used to quote fields containing special characters, such as the delimiter or quotechar, or which contain new-line characters. It defaults to single quote (').
---
