# Meltano Hub - Utility Scripts

## API

### `make_files.py`

This script generates the JSON files for the Meltano Hub API.

#### Options

| Option               | Description                               | Example                                                      |
| -------------------- | ----------------------------------------- | ------------------------------------------------------------ |
| `-o`, `--output-dir` | The directory to write the JSON files to. | `./_hub_api`                                                 |
| `--hub-url`          | The URL of the Meltano Hub.               | `https://meltano.com`                                        |
| `--api-url`          | The URL of the API Gateway stage.         | `https://ty9g0lccp8.execute-api.us-west-2.amazonaws.com/dev` |

#### Usage

```bash
export HUB_URL='https://hub.meltano.com'
export API_URL='https://ty9g0lccp8.execute-api.us-west-2.amazonaws.com/dev'
uv run python utility_scripts/api/make_files.py -o _hub_api --hub-url $HUB_URL --api-url $API_URL
```

To sync the files with the target S3 bucket, run the following command:

```bash
aws s3 sync _hub_api s3://<s3-bucket>/hub-api
```
