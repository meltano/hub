## Additional Configuration

If you are using Great Expectations to validate data in a database or warehouse, you
might need to install the appropriate drivers. Common options are supported by Great Expectations
as pip extras, and any additional packages you may want can be added too by configuring
a custom `pip_url` for the `great_expectations` utility:

```bash
# set the _pip_url extra setting
meltano config great_expectations set _pip_url "great_expectations[redshift]; awscli"
# re-install the great_expectations plugin for changes to take effect
meltano install utility great_expectations
```
