import pytest
from hub_utils.meltano_util import MeltanoUtil
import json
import os

def _read_data(file_name):
    path = os.path.dirname(__file__)
    with open(f'{path}/data/{file_name}', 'r') as f:
        return json.load(f)

def test_sdk_about_parsing_1():
    sdk_about_dict = _read_data('tap_apaleo_about.json')

    settings, settings_group_validation, capabilities = MeltanoUtil._parse_sdk_about_settings(sdk_about_dict)
    print(json.dumps(settings))
    assert settings == [
        {
            "name": "client_id",
            "label": "Client Id",
            "description": "",
            "kind": "password"
        },
        {
            "name": "client_secret",
            "label": "Client Secret",
            "description": "",
            "kind": "password"
        },
        {
            "name": "start_date",
            "label": "Start Date",
            "description": "",
            "kind": "date_iso8601"
        }
    ]
    assert set(settings_group_validation[0]) == set(
        [
            "client_id",
            "client_secret",
            "start_date"
        ]
    )
    assert capabilities == [
        "catalog",
        "state",
        "discover",
        "about",
        "stream-maps"
    ]

def test_sdk_about_parsing_2():
    sdk_about_dict = _read_data('tap_meshstack_about.json')
    settings, settings_group_validation, capabilities = MeltanoUtil._parse_sdk_about_settings(sdk_about_dict)
    print(json.dumps(settings))
    assert settings == [
        {
            "name": "federation.auth.username",
            "label": "Federation Auth Username",
            "description": "The HTTP basic auth user to authenticate against the meshObject API for federation",
            "kind": "string"
        },
        {
            "name": "federation.auth.password",
            "label": "Federation Auth Password",
            "description": "The HTTP basic auth password to authenticate against the meshObject API for federation",
            "kind": "password"
        },
        {
            "name": "federation.api_url",
            "label": "Federation Api Url",
            "description": "The url of the meshObject API (excluding the /api prefix!)",
            "kind": "string"
        },
        {
            "name": "another_setting_required",
            "label": "Another Setting Required",
            "description": "Test required",
            "kind": "string"
        },
        {
            "name": "stream_maps",
            "label": "Stream Maps",
            "description": "Config object for stream maps capability.",
            "kind": "object"
        },
        {
            "name": "stream_map_config",
            "label": "Stream Map Config",
            "description": "User-defined config values to be used within map expressions.",
            "kind": "object"
        },
        {
            "name": "flattening_enabled",
            "label": "Flattening Enabled",
            "description": "True to enable schema flattening and automatically expand nested properties.",
            "kind": "boolean"
        },
        {
            "name": "flattening_max_depth",
            "label": "Flattening Max Depth",
            "description": "The max depth to flatten schemas.",
            "kind": "integer"
        }
    ]
    assert set(settings_group_validation[0]) == set(
        [
            "federation.auth.username",
            "federation.auth.password",
            "federation.api_url",
            "another_setting_required",
            "federation"
        ]
    )
    assert capabilities == [
        "catalog",
        "state",
        "discover",
        "about",
        "stream-maps",
        "schema-flattening"
    ]


def test_sdk_about_parsing_airbyte():
    sdk_about_dict = _read_data('airbyte_s3_about.json')

    settings, settings_group_validation, capabilities = MeltanoUtil._parse_sdk_about_settings(sdk_about_dict)
    print(json.dumps(settings))
    assert settings == [
        {
            "name": "airbyte_spec.image",
            "label": "Airbyte Spec Image",
            "description": "Airbyte image to run",
            "kind": "string"
        },
        {
            "name": "airbyte_spec.tag",
            "label": "Airbyte Spec Tag",
            "description": "",
            "kind": "string"
        },
        {
            "name": "connector_config.dataset",
            "label": "Connector Config Dataset",
            "description": "The name of the stream you would like this source to output. Can contain letters, numbers, or underscores.",
            "kind": "string"
        },
        {
            "name": "connector_config.path_pattern",
            "label": "Connector Config Path Pattern",
            "description": "A regular expression which tells the connector which files to replicate. All files which match this pattern will be replicated. Use | to separate multiple patterns. See <a href=\"https://facelessuser.github.io/wcmatch/glob/\" target=\"_blank\">this page</a> to understand pattern syntax (GLOBSTAR and SPLIT flags are enabled). Use pattern <strong>**</strong> to pick up all files.",
            "kind": "string"
        },
        # Format
        {
            "name": "connector_config.format.filetype",
            "label": "Connector Config Format Filetype",
            "description": "csv, parquet",
            "kind": "string"
        },
        {
            "name": "connector_config.format.delimiter",
            "label": "Connector Config Format Delimiter",
            "description": "The character delimiting individual cells in the CSV data. This may only be a 1-character string. For tab-delimited data enter '\\t'.",
            "kind": "string"
        },
        {
            "name": "connector_config.format.columns",
            "label": "Connector Config Format Columns",
            "description": "If you only want to sync a subset of the columns from the file(s), add the columns you want here as a comma-delimited list. Leave it empty to sync all columns.",
            "kind": "array"
        },
        {
            "name": "connector_config.format.buffer_size",
            "label": "Connector Config Format Buffer Size",
            "description": "Perform read buffering when deserializing individual column chunks. By default every group column will be loaded fully to memory. This option can help avoid out-of-memory errors if your data is particularly wide.",
            "kind": "integer"
        },
        # End after tweaks
        {
            "name": "connector_config.schema",
            "label": "Connector Config Schema",
            "description": "Optionally provide a schema to enforce, as a valid JSON string. Ensure this is a mapping of <strong>{ \"column\" : \"type\" }</strong>, where types are valid <a href=\"https://json-schema.org/understanding-json-schema/reference/type.html\" target=\"_blank\">JSON Schema datatypes</a>. Leave as {} to auto-infer the schema.",
            "kind": "string"
        },
        {
            "name": "connector_config.provider.bucket",
            "label": "Connector Config Provider Bucket",
            "description": "Name of the S3 bucket where the file(s) exist.",
            "kind": "password"
        },
        {
            "name": "connector_config.provider.aws_access_key_id",
            "label": "Connector Config Provider Aws Access Key Id",
            "description": "In order to access private Buckets stored on AWS S3, this connector requires credentials with the proper permissions. If accessing publicly available data, this field is not necessary.",
            "kind": "password"
        },
        {
            "name": "connector_config.provider.aws_secret_access_key",
            "label": "Connector Config Provider Aws Secret Access Key",
            "description": "In order to access private Buckets stored on AWS S3, this connector requires credentials with the proper permissions. If accessing publicly available data, this field is not necessary.",
            "kind": "password"
        },
        {
            "name": "connector_config.provider.path_prefix",
            "label": "Connector Config Provider Path Prefix",
            "description": "By providing a path-like prefix (e.g. myFolder/thisTable/) under which all the relevant files sit, we can optimize finding these in S3. This is optional but recommended if your bucket contains many folders/files which you don't need to replicate.",
            "kind": "password"
        },
        {
            "name": "connector_config.provider.endpoint",
            "label": "Connector Config Provider Endpoint",
            "description": "Endpoint to an S3 compatible service. Leave empty to use AWS.",
            "kind": "password"
        },
        {
            "name": "stream_maps",
            "label": "Stream Maps",
            "description": "Config object for stream maps capability. For more information check out [Stream Maps](https://sdk.meltano.com/en/latest/stream_maps.html).",
            "kind": "object"
        },
        {
            "name": "stream_map_config",
            "label": "Stream Map Config",
            "description": "User-defined config values to be used within map expressions.",
            "kind": "object"
        },
        {
            "name": "flattening_enabled",
            "label": "Flattening Enabled",
            "description": "'True' to enable schema flattening and automatically expand nested properties.",
            "kind": "boolean"
        },
        {
            "name": "flattening_max_depth",
            "label": "Flattening Max Depth",
            "description": "The max depth to flatten schemas.",
            "kind": "integer"
        }
    ]
    assert set(settings_group_validation[0]) == set(
        [
            "airbyte_spec.image",
            "connector_config.provider.bucket",
            "connector_config.dataset",
            "connector_config.path_pattern"

        ]
    )
    assert capabilities == [
        "catalog",
        "state",
        "discover",
        "about",
        "stream-maps",
        "schema-flattening"
    ]


def test_airbyte_array_enum_array():
    sdk_about_dict = _read_data('airbyte_array_enum.json')

    settings, settings_group_validation, capabilities = MeltanoUtil._parse_sdk_about_settings(sdk_about_dict)
    print(json.dumps(settings))
    # TODO: Meltano doesnt support array enums as of today
    # assert settings == [
    #     {
    #         "name": "connector_config.metrics",
    #         "label": "Connector Config Metrics",
    #         "description": "Select at least one metric to query.",
    #         "kind": "options",
    #         "options": [
    #             {"label": "Network Cost", "value": "network_cost"},
    #             {"label": "Network Cost Diff", "value": "network_cost_diff"}
    #         ]
    #     }
    # ]
    assert settings == [
        {
            "name": "connector_config.metrics",
            "label": "Connector Config Metrics",
            "description": "Select at least one metric to query.",
            "kind": "array",
        }
    ]
    assert capabilities == [
        "catalog",
        "state",
        "discover",
        "about",
        "stream-maps",
        "schema-flattening"
    ]

def test_airbyte_array_enum_string():
    sdk_about_dict = _read_data('airbyte_string_enum.json')

    settings, settings_group_validation, capabilities = MeltanoUtil._parse_sdk_about_settings(sdk_about_dict)
    print(json.dumps(settings))
    assert settings == [
        {
            "name": "connector_config.region",
            "label": "Connector Config Region",
            "description": "AWS Region of the SQS Queue",
            "kind": "options",
            "options": [
                {"label": "Us East 1", "value": "us-east-1"},
                {"label": "Us East 2", "value": "us-east-2"}
            ]
        }
    ]
    assert capabilities == [
        "catalog",
        "state",
        "discover",
        "about",
        "stream-maps",
        "schema-flattening"
    ]

@pytest.mark.parametrize(
    "input,expected",
    [
        ["aws_access_key_id", "AWS Access Key ID"],
        ["db_name", "Database Name"],
        ["api_url", "API URL"],
    ]
)
def test_get_label(input, expected):
    assert MeltanoUtil()._get_label(input) == expected
