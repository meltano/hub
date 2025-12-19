import json
import os

import pytest

from hub_utils.meltano_util import MeltanoUtil
from hub_utils.utilities import Utilities


def _read_data(file_name):
    path = os.path.dirname(__file__)
    with open(f"{path}/data/{file_name}") as f:
        return json.load(f)


def test_sdk_about_parsing_1():
    sdk_about_dict = _read_data("tap_apaleo_about.json")

    settings, settings_group_validation, capabilities, _ = MeltanoUtil._parse_sdk_about_settings(sdk_about_dict)
    print(json.dumps(settings))
    assert settings == [
        {
            "name": "client_id",
            "label": "Client ID",
            "description": "",
            "kind": "password",
            "sensitive": True,
        },
        {
            "name": "client_secret",
            "label": "Client Secret",
            "description": "",
            "kind": "password",
            "sensitive": True,
        },
        {
            "name": "start_date",
            "label": "Start Date",
            "description": "",
            "kind": "date_iso8601",
        },
    ]
    assert set(settings_group_validation[0]) == set(["client_id", "client_secret", "start_date"])
    assert capabilities == ["catalog", "state", "discover", "about", "stream-maps"]


def test_sdk_about_parsing_2():
    sdk_about_dict = _read_data("tap_meshstack_about.json")
    settings, settings_group_validation, capabilities, _ = MeltanoUtil._parse_sdk_about_settings(sdk_about_dict)
    print(json.dumps(settings))
    assert settings == [
        {
            "name": "federation.auth.username",
            "label": "Federation Auth Username",
            "description": "The HTTP basic auth user to authenticate against the meshObject API for federation",
            "kind": "string",
        },
        {
            "name": "federation.auth.password",
            "label": "Federation Auth Password",
            "description": "The HTTP basic auth password to authenticate against the meshObject API for federation",
            "kind": "password",
            "sensitive": True,
        },
        {
            "name": "federation.api_url",
            "label": "Federation API URL",
            "description": "The url of the meshObject API (excluding the /api prefix!)",
            "kind": "string",
        },
        {
            "name": "another_setting_required",
            "label": "Another Setting Required",
            "description": "Test required",
            "kind": "string",
        },
        {
            "name": "stream_maps",
            "label": "Stream Maps",
            "description": "Config object for stream maps capability.",
            "kind": "object",
        },
        {
            "name": "stream_map_config",
            "label": "Stream Map Config",
            "description": "User-defined config values to be used within map expressions.",
            "kind": "object",
        },
        {
            "name": "flattening_enabled",
            "label": "Flattening Enabled",
            "description": "True to enable schema flattening and automatically expand nested properties.",
            "kind": "boolean",
        },
        {
            "name": "flattening_max_depth",
            "label": "Flattening Max Depth",
            "description": "The max depth to flatten schemas.",
            "kind": "integer",
        },
    ]
    assert set(settings_group_validation[0]) == set(
        [
            "federation.auth.username",
            "federation.auth.password",
            "federation.api_url",
            "another_setting_required",
            "federation",
        ]
    )
    assert capabilities == [
        "catalog",
        "state",
        "discover",
        "about",
        "stream-maps",
        "schema-flattening",
    ]


def test_sdk_about_parsing_3():
    sdk_about_dict = _read_data("tap_with_rich_config_schema.json")

    settings, _, _, _ = MeltanoUtil._parse_sdk_about_settings(sdk_about_dict)

    assert settings == [
        {
            "name": "username",
            "label": "Username",
            "description": "The username to use when authenticating with the API",
            "kind": "string",
        },
        {
            "name": "password",
            "label": "Password",
            "description": "The password to use when authenticating with the API",
            "kind": "password",
            "sensitive": True,
        },
        {
            "name": "cmo",
            "label": "Client Management Organization",
            "description": "The client management organization to use when authenticating with the API",
            "kind": "string",
        },
    ]


def test_sdk_about_dependent_required():
    sdk_about_dict = {
        "name": "tap-example",
        "description": "Singer.io tap for extracting data from example",
        "version": "0.1.0",
        "sdk_version": "0.40.0",
        "capabilities": [
            "catalog",
            "state",
            "discover",
            "about",
            "stream-maps",
            "schema-flattening",
        ],
        "settings": {
            "type": "object",
            "properties": {
                "username": {
                    "description": "The username to use when authenticating with the API",
                    "title": "Username",
                    "type": [
                        "string",
                        "null",
                    ],
                },
                "password": {
                    "description": "The password to use when authenticating with the API",
                    "title": "Password",
                    "type": ["string", "null"],
                    "secret": True,
                    "writeOnly": True,
                },
                "client_id": {
                    "description": "The client ID to use when authenticating with the API",
                    "title": "Client ID",
                    "type": [
                        "string",
                        "null",
                    ],
                },
                "client_secret": {
                    "description": "The client secret to use when authenticating with the API",
                    "title": "Client Secret",
                    "type": [
                        "string",
                        "null",
                    ],
                    "secret": True,
                    "writeOnly": True,
                },
                "refresh_token": {
                    "description": "The refresh token to use when authenticating with the API",
                    "title": "Refresh Token",
                    "type": ["string", "null"],
                    "secret": True,
                    "writeOnly": True,
                },
                "cmo": {
                    "description": "The client management organization to use when authenticating with the API",
                    "title": "Client Management Organization",
                    "type": ["string", "null"],
                },
            },
            "dependentRequired": {
                "username": ["password"],
                "client_id": ["client_secret", "refresh_token"],
            },
        },
    }

    settings, settings_group_validation, _, _ = MeltanoUtil._parse_sdk_about_settings(sdk_about_dict)

    assert settings == [
        {
            "name": "username",
            "label": "Username",
            "description": "The username to use when authenticating with the API",
            "kind": "string",
        },
        {
            "name": "password",
            "label": "Password",
            "description": "The password to use when authenticating with the API",
            "kind": "password",
            "sensitive": True,
        },
        {
            "name": "client_id",
            "label": "Client ID",
            "description": "The client ID to use when authenticating with the API",
            "kind": "password",
            "sensitive": True,
        },
        {
            "name": "client_secret",
            "label": "Client Secret",
            "description": "The client secret to use when authenticating with the API",
            "kind": "password",
            "sensitive": True,
        },
        {
            "name": "refresh_token",
            "label": "Refresh Token",
            "description": "The refresh token to use when authenticating with the API",
            "kind": "password",
            "sensitive": True,
        },
        {
            "name": "cmo",
            "label": "Client Management Organization",
            "description": "The client management organization to use when authenticating with the API",
            "kind": "string",
        },
    ]

    assert settings_group_validation == [
        ["username", "password"],
        ["client_id", "client_secret", "refresh_token"],
    ]


def test_sdk_about_dependent_required_nested():
    sdk_about_dict = {
        "name": "tap-example",
        "description": "Singer.io tap for extracting data from example",
        "version": "0.1.0",
        "sdk_version": "0.40.0",
        "capabilities": [
            "catalog",
            "state",
            "discover",
            "about",
            "stream-maps",
            "schema-flattening",
        ],
        "settings": {
            "type": "object",
            "properties": {
                "cmo": {
                    "description": "The client management organization to use when authenticating with the API",
                    "title": "Client Management Organization",
                    "type": ["string", "null"],
                },
                "auth": {
                    "type": "object",
                    "properties": {
                        "username": {
                            "description": "The username to use when authenticating with the API",
                            "title": "Username",
                            "type": [
                                "string",
                                "null",
                            ],
                        },
                        "password": {
                            "description": "The password to use when authenticating with the API",
                            "title": "Password",
                            "type": ["string", "null"],
                            "secret": True,
                            "writeOnly": True,
                        },
                        "client_id": {
                            "description": "The client ID to use when authenticating with the API",
                            "title": "Client ID",
                            "type": [
                                "string",
                                "null",
                            ],
                        },
                        "client_secret": {
                            "description": "The client secret to use when authenticating with the API",
                            "title": "Client Secret",
                            "type": [
                                "string",
                                "null",
                            ],
                            "secret": True,
                            "writeOnly": True,
                        },
                        "refresh_token": {
                            "description": "The refresh token to use when authenticating with the API",
                            "title": "Refresh Token",
                            "type": ["string", "null"],
                            "secret": True,
                            "writeOnly": True,
                        },
                    },
                    "dependentRequired": {
                        "username": ["password"],
                        "client_id": ["client_secret", "refresh_token"],
                    },
                },
            },
        },
    }

    settings, settings_group_validation, _, _ = MeltanoUtil._parse_sdk_about_settings(sdk_about_dict)

    assert settings == [
        {
            "name": "cmo",
            "label": "Client Management Organization",
            "description": "The client management organization to use when authenticating with the API",
            "kind": "string",
        },
        {
            "name": "auth.username",
            "label": "Username",
            "description": "The username to use when authenticating with the API",
            "kind": "string",
        },
        {
            "name": "auth.password",
            "label": "Password",
            "description": "The password to use when authenticating with the API",
            "kind": "password",
            "sensitive": True,
        },
        {
            "name": "auth.client_id",
            "label": "Client ID",
            "description": "The client ID to use when authenticating with the API",
            "kind": "password",
            "sensitive": True,
        },
        {
            "name": "auth.client_secret",
            "label": "Client Secret",
            "description": "The client secret to use when authenticating with the API",
            "kind": "password",
            "sensitive": True,
        },
        {
            "name": "auth.refresh_token",
            "label": "Refresh Token",
            "description": "The refresh token to use when authenticating with the API",
            "kind": "password",
            "sensitive": True,
        },
    ]

    assert settings_group_validation == [
        ["auth.username", "auth.password"],
        ["auth.client_id", "auth.client_secret", "auth.refresh_token"],
    ]


def test_sdk_about_parsing_airbyte():
    sdk_about_dict = _read_data("airbyte_s3_about.json")

    settings, settings_group_validation, capabilities, _ = MeltanoUtil._parse_sdk_about_settings(sdk_about_dict)
    print(json.dumps(settings))
    expected_settings = [
        {
            "name": "airbyte_spec.image",
            "label": "Airbyte Spec Image",
            "description": "Airbyte image to run",
            "kind": "string",
        },
        {
            "name": "airbyte_spec.tag",
            "label": "Airbyte Spec Tag",
            "description": "",
            "kind": "string",
            "value": "latest",
        },
        {
            "name": "connector_config.dataset",
            "label": "Output Stream Name",
            "description": "The name of the stream you would like this source to output. Can contain letters, numbers, or underscores.",  # noqa: E501
            "kind": "string",
        },
        {
            "name": "connector_config.path_pattern",
            "label": "Pattern of files to replicate",
            "description": 'A regular expression which tells the connector which files to replicate. All files which match this pattern will be replicated. Use | to separate multiple patterns. See <a href="https://facelessuser.github.io/wcmatch/glob/" target="_blank">this page</a> to understand pattern syntax (GLOBSTAR and SPLIT flags are enabled). Use pattern <strong>**</strong> to pick up all files.',  # noqa: E501
            "kind": "string",
        },
        # Format
        {
            "name": "connector_config.format.filetype",
            "label": "Filetype",
            "description": "Csv, Parquet",
            "kind": "string",
        },
        {
            "name": "connector_config.format.delimiter",
            "label": "Delimiter",
            "description": "The character delimiting individual cells in the CSV data. This may only be a 1-character string. For tab-delimited data enter '\\t'.",  # noqa: E501
            "kind": "string",
            "value": ",",
        },
        {
            "name": "connector_config.format.columns",
            "label": "Selected Columns",
            "description": "If you only want to sync a subset of the columns from the file(s), add the columns you want here as a comma-delimited list. Leave it empty to sync all columns.",  # noqa: E501
            "kind": "array",
        },
        {
            "name": "connector_config.format.buffer_size",
            "label": "Buffer Size",
            "description": "Perform read buffering when deserializing individual column chunks. By default every group column will be loaded fully to memory. This option can help avoid out-of-memory errors if your data is particularly wide.",  # noqa: E501
            "kind": "integer",
            "value": 2,
        },
        # End after tweaks
        {
            "name": "connector_config.schema",
            "label": "Manually enforced data schema",
            "description": 'Optionally provide a schema to enforce, as a valid JSON string. Ensure this is a mapping of <strong>{ "column" : "type" }</strong>, where types are valid <a href="https://json-schema.org/understanding-json-schema/reference/type.html" target="_blank">JSON Schema datatypes</a>. Leave as {} to auto-infer the schema.',  # noqa: E501
            "kind": "string",
            "value": "{}",
        },
        {
            "name": "connector_config.provider.bucket",
            "label": "Bucket",
            "description": "Name of the S3 bucket where the file(s) exist.",
            "kind": "password",
            "sensitive": True,
        },
        {
            "name": "connector_config.provider.aws_access_key_id",
            "label": "AWS Access Key ID",
            "description": "In order to access private Buckets stored on AWS S3, this connector requires credentials with the proper permissions. If accessing publicly available data, this field is not necessary.",  # noqa: E501
            "kind": "password",
            "sensitive": True,
        },
        {
            "name": "connector_config.provider.aws_secret_access_key",
            "label": "AWS Secret Access Key",
            "description": "In order to access private Buckets stored on AWS S3, this connector requires credentials with the proper permissions. If accessing publicly available data, this field is not necessary.",  # noqa: E501
            "kind": "password",
            "sensitive": True,
        },
        {
            "name": "connector_config.provider.path_prefix",
            "label": "Path Prefix",
            "description": "By providing a path-like prefix (e.g. myFolder/thisTable/) under which all the relevant files sit, we can optimize finding these in S3. This is optional but recommended if your bucket contains many folders/files which you don't need to replicate.",  # noqa: E501
            "kind": "password",
            "sensitive": True,
            "value": "",
        },
        {
            "name": "connector_config.provider.endpoint",
            "label": "Endpoint",
            "description": "Endpoint to an S3 compatible service. Leave empty to use AWS.",
            "kind": "password",
            "sensitive": True,
            "value": "",
        },
        {
            "name": "stream_maps",
            "label": "Stream Maps",
            "description": "Config object for stream maps capability. For more information check out [Stream Maps](https://sdk.meltano.com/en/latest/stream_maps.html).",
            "kind": "object",
        },
        {
            "name": "stream_map_config",
            "label": "Stream Map Config",
            "description": "User-defined config values to be used within map expressions.",
            "kind": "object",
        },
        {
            "name": "flattening_enabled",
            "label": "Flattening Enabled",
            "description": "'True' to enable schema flattening and automatically expand nested properties.",
            "kind": "boolean",
        },
        {
            "name": "flattening_max_depth",
            "label": "Flattening Max Depth",
            "description": "The max depth to flatten schemas.",
            "kind": "integer",
        },
    ]
    for i, setting in enumerate(settings):
        assert setting == expected_settings[i], setting
    assert set(settings_group_validation[0]) == set(
        [
            "airbyte_spec.image",
            "connector_config.provider.bucket",
            "connector_config.dataset",
            "connector_config.path_pattern",
        ]
    )
    assert capabilities == [
        "catalog",
        "state",
        "discover",
        "about",
        "stream-maps",
        "schema-flattening",
    ]


def test_airbyte_array_enum_array():
    sdk_about_dict = _read_data("airbyte_array_enum.json")

    settings, settings_group_validation, capabilities, _ = MeltanoUtil._parse_sdk_about_settings(sdk_about_dict)
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
            "label": "Metrics to ingest",
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
        "schema-flattening",
    ]


def test_airbyte_array_enum_string():
    sdk_about_dict = _read_data("airbyte_string_enum.json")

    settings, settings_group_validation, capabilities, _ = MeltanoUtil._parse_sdk_about_settings(sdk_about_dict)
    print(json.dumps(settings))
    assert settings == [
        {
            "name": "connector_config.region",
            "label": "AWS Region",
            "description": "AWS Region of the SQS Queue",
            "kind": "options",
            "options": [
                {"label": "Us East 1", "value": "us-east-1"},
                {"label": "Us East 2", "value": "us-east-2"},
            ],
        }
    ]
    assert capabilities == [
        "catalog",
        "state",
        "discover",
        "about",
        "stream-maps",
        "schema-flattening",
    ]


@pytest.mark.parametrize(
    "input,expected",
    [
        ["aws_access_key_id", "AWS Access Key ID"],
        ["db_name", "Database Name"],
        ["api_url", "API URL"],
        ["oauth_credentials.client_secret", "OAuth Credentials Client Secret"],
    ],
)
def test_get_label(input, expected):
    assert MeltanoUtil()._get_label(input) == expected


def test_sdk_about_parsing_default():
    input = {
        "settings": {
            "type": "object",
            "properties": {
                "test": {
                    "type": ["string"],
                    "default": "my default",
                    "description": "my description",
                }
            },
            "required": [],
        }
    }
    settings, _, _, _ = MeltanoUtil._parse_sdk_about_settings(input)
    assert settings == [
        {
            "name": "test",
            "label": "Test",
            "description": "My description",
            "kind": "string",
            "value": "my default",
        }
    ]


def test_sdk_about_parsing_default_bool():
    input = {
        "settings": {
            "type": "object",
            "properties": {
                "test": {
                    "type": ["string"],
                    "default": False,
                    "description": "my description",
                }
            },
            "required": [],
        }
    }
    settings, _, _, _ = MeltanoUtil._parse_sdk_about_settings(input)
    assert settings == [
        {
            "name": "test",
            "label": "Test",
            "description": "My description",
            "kind": "string",
            "value": False,
        }
    ]


def test_sdk_about_parsing_skip_default_dates():
    input = {
        "settings": {
            "type": "object",
            "properties": {
                "start_date": {
                    "type": ["string", "null"],
                    "format": "date-time",
                    "default": "2020-04-04T19:54:26.375510Z",
                    "description": "The description",
                },
                "end_date": {
                    "type": ["string", "null"],
                    "format": "date-time",
                    "default": "2020-04-04T19:54:26.375510Z",
                    "description": "The description",
                },
            },
            "required": [],
        }
    }
    settings, _, _, _ = MeltanoUtil._parse_sdk_about_settings(input)
    assert settings == [
        {
            "name": "start_date",
            "label": "Start Date",
            "description": "The description",
            "kind": "date_iso8601",
        },
        {
            "name": "end_date",
            "label": "End Date",
            "description": "The description",
            "kind": "date_iso8601",
        },
    ]


@pytest.mark.parametrize(
    "input,expected",
    [
        # Official
        [["meltanolabs", True, 0, "low"], "gold"],
        [["meltanolabs", True, 0, "medium"], "gold"],
        [["meltanolabs", True, 0, "high"], "gold"],
        [["meltanolabs", True, 1, "low"], "gold"],
        [["meltanolabs", True, 1, "medium"], "gold"],
        [["meltanolabs", True, 1, "high"], "gold"],
        [["meltanolabs", True, 6, "low"], "gold"],
        [["meltanolabs", True, 6, "medium"], "gold"],
        [["meltanolabs", True, 6, "high"], "gold"],
        [["meltanolabs", False, 0, "low"], "bronze"],
        [["meltanolabs", False, 0, "medium"], "bronze"],
        [["meltanolabs", False, 0, "high"], "bronze"],
        [["meltanolabs", False, 1, "low"], "bronze"],
        [["meltanolabs", False, 1, "medium"], "silver"],
        [["meltanolabs", False, 1, "high"], "silver"],
        [["meltanolabs", False, 6, "low"], "bronze"],
        [["meltanolabs", False, 6, "medium"], "silver"],
        [["meltanolabs", False, 6, "high"], "silver"],
        # Partner
        [["matatika", True, 0, "low"], "gold"],
        [["matatika", True, 0, "medium"], "gold"],
        [["matatika", True, 0, "high"], "gold"],
        [["matatika", True, 1, "low"], "gold"],
        [["matatika", True, 1, "medium"], "gold"],
        [["matatika", True, 1, "high"], "gold"],
        [["matatika", True, 6, "low"], "gold"],
        [["matatika", True, 6, "medium"], "gold"],
        [["matatika", True, 6, "high"], "gold"],
        [["matatika", False, 0, "low"], "bronze"],
        [["matatika", False, 0, "medium"], "bronze"],
        [["matatika", False, 0, "high"], "bronze"],
        [["matatika", False, 1, "low"], "bronze"],
        [["matatika", False, 1, "medium"], "silver"],
        [["matatika", False, 1, "high"], "silver"],
        [["matatika", False, 6, "low"], "bronze"],
        [["matatika", False, 6, "medium"], "silver"],
        [["matatika", False, 6, "high"], "silver"],
        # Community
        [["foobar", True, 0, "low"], "silver"],
        [["foobar", True, 0, "medium"], "silver"],
        [["foobar", True, 0, "high"], "silver"],
        [["foobar", True, 1, "low"], "silver"],
        [["foobar", True, 1, "medium"], "silver"],
        [["foobar", True, 1, "high"], "silver"],
        [["foobar", True, 6, "low"], "silver"],
        [["foobar", True, 6, "medium"], "gold"],
        [["foobar", True, 6, "high"], "gold"],
        [["foobar", False, 0, "low"], "unknown"],
        [["foobar", False, 0, "medium"], "unknown"],
        [["foobar", False, 0, "high"], "unknown"],
        [["foobar", False, 1, "low"], "bronze"],
        [["foobar", False, 1, "medium"], "silver"],
        [["foobar", False, 1, "high"], "silver"],
        [["foobar", False, 6, "low"], "bronze"],
        [["foobar", False, 6, "medium"], "silver"],
        [["foobar", False, 6, "high"], "silver"],
        # Singer
        [["singer-io", False, 0, "low"], "bronze"],
        # Airbyte
        [["airbyte", False, 0, "low"], "bronze"],
        # Transferwise
        [["transferwise", False, 6, "low"], "silver"],
        [["transferwise", False, 1, "medium"], "silver"],
        [["transferwise", False, 0, "low"], "bronze"],
    ],
)
def test_get_quality(input, expected):
    assert MeltanoUtil.get_quality(*input) == expected, input


@pytest.mark.parametrize(
    "input,expected",
    [
        ["foo.Test.", "Foo. Test."],
        [
            "default 3,600 seconds (i.e. 1 hour). Something.",
            "Default 3,600 seconds (i.e. 1 hour). Something.",
        ],
        [
            "Data was scanned ~1.5 times for that batch.",
            "Data was scanned ~1.5 times for that batch.",
        ],
        ["dbt is the best. Dbt is good.", "dbt is the best. dbt is good."],
        ["Path to .duckdb file", "Path to .duckdb file"],
        ["Foo .env file.", "Foo .env file."],
        [
            "By (e.g. myFolder/thisTable/) sit, S3. This is replicate.",
            "By (e.g. myFolder/thisTable/) sit, S3. This is replicate.",
        ],
        [
            "Request timeout used when not overridden in Session.execute().",
            "Request timeout used when not overridden in Session.execute().",
        ],
        [
            'For example, "from:someuser@example.com rfc822msgid:<somemsgid@example.com> is:unread"."',
            'For example, "from:someuser@example.com rfc822msgid:<somemsgid@example.com> is:unread"."',
        ],
        [
            "tap-saasoptics <api_user_email@your_company.com>.",
            "tap-saasoptics <api_user_email@your_company.com>.",
        ],
        ["https://api.totango.com", "https://api.totango.com"],
    ],
)
def test_clean_description(input, expected):
    assert MeltanoUtil._clean_description(input) == expected


def test_sdk_about_parsing_faker_configs():
    sdk_about_dict = _read_data("faker_configs.json")
    settings, _, _, _ = MeltanoUtil._parse_sdk_about_settings(sdk_about_dict)
    assert settings == [
        {
            "name": "faker_config.seed",
            "label": "Faker Config Seed",
            "description": "Value to seed the Faker generator for deterministic output: https://faker.readthedocs.io/en/master/#seeding-the-generator",
            "kind": "string",
        },
        {
            "name": "faker_config.locale",
            "label": "Faker Config Locale",
            "description": "One or more LCID locale strings to produce localized output for: https://faker.readthedocs.io/en/master/#localization",
            "kind": "array",
        },
    ]


def test_log_parser_property_with_structured_logging():
    """Test that log_parser property is added when structured-logging capability is present."""
    # Create mock SDK about data with structured-logging capability
    sdk_about_dict = {
        "name": "tap-example",
        "capabilities": ["catalog", "discover", "state", "structured-logging"],
        "settings": {
            "properties": {"api_key": {"type": "string", "title": "API Key", "description": "Your API key"}},
            "required": ["api_key"],
        },
    }

    # Parse SDK about info
    settings, validation_groups, capabilities, _ = MeltanoUtil._parse_sdk_about_settings(sdk_about_dict)

    # Create plugin definition using utilities
    utils = Utilities(auto_accept=True)
    plugin_def = utils._boilerplate_definition(
        repo_url="https://github.com/example/tap-example",
        plugin_type="extractors",
        settings=settings,
        settings_group_validation=validation_groups,
        name="tap-example",
        namespace="tap_example",
        pip_url="tap-example",
        keywords=["example", "api", "meltano_sdk"],
        capabilities=capabilities,
        executable="tap-example",
        variant="meltanolabs",
    )

    # Verify log_parser property is added
    assert "log_parser" in plugin_def
    assert plugin_def["log_parser"] == "singer-sdk"
    assert "structured-logging" in plugin_def["capabilities"]


def test_log_parser_property_without_structured_logging():
    """Test that log_parser property is NOT added when structured-logging capability is absent."""
    # Create mock SDK about data WITHOUT structured-logging capability
    sdk_about_dict = {
        "name": "tap-legacy",
        "capabilities": ["catalog", "discover", "state"],
        "settings": {
            "properties": {"api_key": {"type": "string", "title": "API Key", "description": "Your API key"}},
            "required": ["api_key"],
        },
    }

    # Parse SDK about info
    settings, validation_groups, capabilities, _ = MeltanoUtil._parse_sdk_about_settings(sdk_about_dict)

    # Create plugin definition using utilities
    utils = Utilities(auto_accept=True)
    plugin_def = utils._boilerplate_definition(
        repo_url="https://github.com/example/tap-legacy",
        plugin_type="extractors",
        settings=settings,
        settings_group_validation=validation_groups,
        name="tap-legacy",
        namespace="tap_legacy",
        pip_url="tap-legacy",
        keywords=["legacy"],
        capabilities=capabilities,
        executable="tap-legacy",
        variant="community",
    )

    # Verify log_parser property is NOT added
    assert "log_parser" not in plugin_def
    assert "structured-logging" not in plugin_def["capabilities"]


def test_log_parser_property_with_mixed_capabilities():
    """Test log_parser property with plugin that has many capabilities including structured-logging."""
    # Create mock SDK about data with many capabilities including structured-logging
    sdk_about_dict = {
        "name": "tap-comprehensive",
        "capabilities": [
            "catalog",
            "discover",
            "state",
            "about",
            "stream-maps",
            "schema-flattening",
            "batch",
            "structured-logging",
        ],
        "settings": {
            "properties": {
                "database_url": {"type": "string", "title": "Database URL", "description": "Database connection URL"}
            },
            "required": ["database_url"],
        },
    }

    # Parse SDK about info
    settings, validation_groups, capabilities, _ = MeltanoUtil._parse_sdk_about_settings(sdk_about_dict)

    # Create plugin definition using utilities
    utils = Utilities(auto_accept=True)
    plugin_def = utils._boilerplate_definition(
        repo_url="https://github.com/example/tap-comprehensive",
        plugin_type="extractors",
        settings=settings,
        settings_group_validation=validation_groups,
        name="tap-comprehensive",
        namespace="tap_comprehensive",
        pip_url="tap-comprehensive",
        keywords=["comprehensive", "database", "meltano_sdk"],
        capabilities=capabilities,
        executable="tap-comprehensive",
        variant="meltanolabs",
    )

    # Verify log_parser property is added and all capabilities are preserved
    assert "log_parser" in plugin_def
    assert plugin_def["log_parser"] == "singer-sdk"
    assert "structured-logging" in plugin_def["capabilities"]
    assert len(plugin_def["capabilities"]) == 8  # All original capabilities preserved
    assert set(plugin_def["capabilities"]) == set(sdk_about_dict["capabilities"])


def test_log_parser_property_non_sdk_with_structured_logging():
    """Test that log_parser property is NOT added for non-SDK plugin with structured-logging capability."""
    # Create mock SDK about data with structured-logging capability but no SDK keyword
    sdk_about_dict = {
        "name": "tap-non-sdk",
        "capabilities": ["catalog", "discover", "state", "structured-logging"],
        "settings": {
            "properties": {
                "config_file": {"type": "string", "title": "Config File", "description": "Path to configuration file"}
            },
            "required": ["config_file"],
        },
    }

    # Parse SDK about info
    settings, validation_groups, capabilities, _ = MeltanoUtil._parse_sdk_about_settings(sdk_about_dict)

    # Create plugin definition using utilities (without meltano_sdk keyword)
    utils = Utilities(auto_accept=True)
    plugin_def = utils._boilerplate_definition(
        repo_url="https://github.com/example/tap-non-sdk",
        plugin_type="extractors",
        settings=settings,
        settings_group_validation=validation_groups,
        name="tap-non-sdk",
        namespace="tap_non_sdk",
        pip_url="tap-non-sdk",
        keywords=["legacy", "non-sdk"],  # No meltano_sdk keyword
        capabilities=capabilities,
        executable="tap-non-sdk",
        variant="community",
    )

    # Verify log_parser property is NOT added even though structured-logging is present
    assert "log_parser" not in plugin_def
    assert "structured-logging" in plugin_def["capabilities"]
    assert "meltano_sdk" not in plugin_def["keywords"]
