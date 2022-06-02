## Additional Setup Instructions

### How to get your Customer ID(s)

Customer ID(s) are also known as Account ID(s).

To get your Account ID(s):

1. Visit the Google Ads management interface: <https://ads.google.com/>
2. Log in if you haven't already.
3. Make sure the correct account is selected in the top left corner.

![Screenshot of account selector](/assets/images/tap-adwords/account-selector.png)

4. You will see the Account ID displayed inside the selector to the right of the account name, with added dashes for readability.

Remove the dashes before you enter the ID in Meltano: `205-667-8813` becomes `2056678813`.

If you want to extract data from multiple Ad Accounts, repeat the steps above to find the IDs (without dashes), and enter them in Meltano separated by commas (`,`).

For example:

- One Account ID: `1234567890`
- Multiple Account IDs: `1234567890,1234567891,1234567892`

### How to use Primary Keys

Manage this setting directly in your [`meltano.yml` project file](https://docs.meltano.com/concepts/project#meltano-yml-project-file):

```yml{5-8}
plugins:
  extractors:
  - name: tap-adwords
    variant: singer-io
    config:
      primary_keys:
        <REPORT_NAME>: [<key1>, <key2>]
        # ...
```

Alternatively, manage this setting using [`meltano config`](https://docs.meltano.com/command-line-interface.html#config) or an [environment variable](https://docs.meltano.com/configuration.html#configuring-settings):

```bash
meltano config tap-adwords set primary_keys <REPORT_NAME> '["<key>", ...]'

export TAP_ADWORDS_PRIMARY_KEYS='{"<REPORT_NAME>": ["<key>", ...], ...}'

# Once primary keys have been set in `meltano.yml`, environment variables can be used
# to override specific nested properties:
export TAP_ADWORDS_PRIMARY_KEYS_<REPORT_NAME>=='["<key>", ...]'

# For example:
meltano config tap-adwords set primary_keys KEYWORDS_PERFORMANCE_REPORT '["customerID"]'

export TAP_ADWORDS_PRIMARY_KEYS_KEYWORDS_PERFORMANCE_REPORT='["customerID"]'
```
