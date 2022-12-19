import pytest
from hub_utils.meltano_util import MeltanoUtil
import json


def test_sdk_about_parsing_1():
    sdk_about_dict = {
        "name": "tap-apaleo",
        "description": "Apaleo tap class.",
        "version": "0.0.1",
        "sdk_version": "0.3.18",
        "capabilities": [
            "catalog",
            "state",
            "discover",
            "about",
            "stream-maps"
        ],
        "settings": {
            "type": "object",
            "properties": {
            "client_id": {
                "type": [
                "string"
                ]
            },
            "client_secret": {
                "type": [
                "string"
                ]
            },
            "start_date": {
                "type": [
                "string"
                ],
                "format": "date-time"
            }
            },
            "required": [
                "client_id",
                "client_secret",
                "start_date"
            ]
        }
    }

    settings, settings_group_validation, capabilities = MeltanoUtil._parse_sdk_about_settings(sdk_about_dict)
    print(json.dumps(settings))
    assert settings == [
        {
            "name": "client_id",
            "label": "Client Id",
            "description": None,
            "kind": "password"
        },
        {
            "name": "client_secret",
            "label": "Client Secret",
            "description": None,
            "kind": "password"
        },
        {
            "name": "start_date",
            "label": "Start Date",
            "description": None,
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
    sdk_about_dict = {
        "name": "tap-meshstack",
        "description": "meshStack tap class.",
        "version": "0.0.1",
        "sdk_version": "0.4.9",
        "capabilities": [
            "catalog",
            "state",
            "discover",
            "about",
            "stream-maps",
            "schema-flattening"
        ],
        "settings": {
        "type": "object",
        "properties": {
            "federation": {
            "type": "object",
            "properties": {
                "auth": {
                "type": "object",
                "properties": {
                    "username": {
                    "type": [
                        "string"
                    ],
                    "description": "The HTTP basic auth user to authenticate against the meshObject API for federation"
                    },
                    "password": {
                    "type": [
                        "string"
                    ],
                    "description": "The HTTP basic auth password to authenticate against the meshObject API for federation"
                    }
                },
                "required": [
                    "username",
                    "password"
                ],
                "description": "API authentication configuration"
                },
                "api_url": {
                "type": [
                    "string"
                ],
                "description": "The url of the meshObject API (excluding the /api prefix!)"
                }
            },
            "required": [
                "auth",
                "api_url"
            ],
            "description": "Configuration for Federation"
            },
            "another_setting_required": {
            "type": [
                "string",
                "null"
            ],
            "description": "Test required"
            },
            "stream_maps": {
            "type": [
                "object",
                "null"
            ],
            "properties": {},
            "description": "Config object for stream maps capability."
            },
            "stream_map_config": {
            "type": [
                "object",
                "null"
            ],
            "properties": {},
            "description": "User-defined config values to be used within map expressions."
            },
            "flattening_enabled": {
            "type": [
                "boolean",
                "null"
            ],
            "description": "True to enable schema flattening and automatically expand nested properties."
            },
            "flattening_max_depth": {
            "type": [
                "integer",
                "null"
            ],
            "description": "The max depth to flatten schemas."
            }
        },
        "required": [
            "federation",
            "another_setting_required"
        ]
        }
    }

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
