from unittest.mock import patch

import pytest

from hub_utils.utilities import Utilities


def test_get_plugin_type_from_suffix():
    utils = Utilities()
    plugin_type = utils.get_plugin_type_from_suffix("extractors/tap-csv/meltanolabs")
    assert plugin_type == "extractors"


def test_get_plugin_variant_from_suffix():
    utils = Utilities()
    variant = utils.get_plugin_variant_from_suffix("extractors/tap-csv/meltanolabs")
    assert variant == "meltanolabs"


@patch.object(Utilities, "_write_updated_def")
def test_merge_and_update(patch):
    utils = Utilities()
    utils.merge_and_update(
        {
            "keywords": ["keys"],
            "maintenance_status": "active",
            "settings": [
                {
                    "name": "add_metadata_columns",
                    "description": "The description",
                    "label": "Add Metadata Columns",
                    "kind": "boolean",
                }
            ],
        },
        "tap-csv",
        "extractors",
        "meltanolabs",
        [
            {
                "name": "add_metadata_columns",
                "description": "The description",
                "label": "Add Metadata Columns",
                "kind": "boolean",
            }
        ],
        ["catalog", "discover"],
        [
            [
                "files",
            ],
            [
                "csv_files_definition",
            ],
        ],
    )
    patch.assert_called_with(
        "tap-csv",
        "meltanolabs",
        "extractors",
        {
            "capabilities": ["catalog", "discover"],
            "keywords": ["keys"],
            "maintenance_status": "active",
            "settings": [
                {
                    "description": "The description",
                    "kind": "boolean",
                    "label": "Add Metadata Columns",
                    "name": "add_metadata_columns",
                }
            ],
            "settings_group_validation": [["files"], ["csv_files_definition"]],
        },
    )


@patch.object(Utilities, "_write_updated_def")
def test_merge_and_update_manual_sgv(patch):
    utils = Utilities()
    utils.merge_and_update(
        {
            "keywords": ["keys"],
            "maintenance_status": "active",
            "settings": [
                {
                    "name": "add_metadata_columns",
                    "description": "The description",
                    "label": "Add Metadata Columns",
                    "kind": "boolean",
                }
            ],
            "settings_group_validation": [
                ["key_file_location", "start_date", "view_id"],
                ["client_secrets", "start_date", "view_id"],
                [
                    "oauth_credentials.access_token",
                    "oauth_credentials.client_id",
                    "oauth_credentials.client_secret",
                    "oauth_credentials.refresh_token",
                    "start_date",
                    "view_id",
                ],
            ],
        },
        "tap-csv",
        "extractors",
        "meltanolabs",
        [
            {
                "name": "add_metadata_columns",
                "description": "The description",
                "label": "Add Metadata Columns",
                "kind": "boolean",
            }
        ],
        ["catalog", "discover"],
        [
            [
                "files",
            ],
            [
                "csv_files_definition",
            ],
        ],
    )
    patch.assert_called_with(
        "tap-csv",
        "meltanolabs",
        "extractors",
        {
            "capabilities": ["catalog", "discover"],
            "keywords": ["keys"],
            "maintenance_status": "active",
            "settings": [
                {
                    "description": "The description",
                    "kind": "boolean",
                    "label": "Add Metadata Columns",
                    "name": "add_metadata_columns",
                }
            ],
            "settings_group_validation": [
                ["key_file_location", "start_date", "view_id"],
                ["client_secrets", "start_date", "view_id"],
                [
                    "oauth_credentials.access_token",
                    "oauth_credentials.client_id",
                    "oauth_credentials.client_secret",
                    "oauth_credentials.refresh_token",
                    "start_date",
                    "view_id",
                ],
            ],
        },
    )


@pytest.mark.parametrize(
    "existing,new,expected",
    [
        # Nothing changes
        [
            [
                {
                    "name": "add_metadata_columns",
                    "description": "The description",
                    "label": "Add Metadata Columns",
                    "kind": "boolean",
                }
            ],
            [
                {
                    "name": "add_metadata_columns",
                    "description": "The description",
                    "label": "Add Metadata Columns",
                    "kind": "boolean",
                }
            ],
            [
                {
                    "name": "add_metadata_columns",
                    "description": "The description",
                    "label": "Add Metadata Columns",
                    "kind": "boolean",
                }
            ],
        ],
        # Setting removed
        [
            [
                {
                    "name": "add_metadata_columns",
                    "description": "The description",
                    "label": "Add Metadata Columns",
                    "kind": "boolean",
                }
            ],
            [],
            [],
        ],
        # Setting added
        [
            [],
            [
                {
                    "name": "add_metadata_columns",
                    "description": "The description",
                    "label": "Add Metadata Columns",
                    "kind": "boolean",
                }
            ],
            [
                {
                    "name": "add_metadata_columns",
                    "description": "The description",
                    "label": "Add Metadata Columns",
                    "kind": "boolean",
                }
            ],
        ],
        # Description changed
        [
            [
                {
                    "name": "add_metadata_columns",
                    "description": "Original",
                    "label": "Add Metadata Columns",
                    "kind": "boolean",
                }
            ],
            [
                {
                    "name": "add_metadata_columns",
                    "description": "New",
                    "label": "Add Metadata Columns",
                    "kind": "boolean",
                }
            ],
            [
                {
                    "name": "add_metadata_columns",
                    "description": "New",
                    "label": "Add Metadata Columns",
                    "kind": "boolean",
                }
            ],
        ],
        # Preserve manually added attributes
        [
            [
                {
                    "name": "add_metadata_columns",
                    "description": "The description",
                    "label": "Add Metadata Columns",
                    "kind": "boolean",
                    "value": "$MELTANO_EXTRACT__LOAD_SCHEMA",
                    "placeholder": "foo",
                    "documentation": "bar",
                }
            ],
            [
                {
                    "name": "add_metadata_columns",
                    "description": "The description",
                    "label": "Add Metadata Columns",
                    "kind": "boolean",
                }
            ],
            [
                {
                    "name": "add_metadata_columns",
                    "description": "The description",
                    "label": "Add Metadata Columns",
                    "kind": "boolean",
                    "value": "$MELTANO_EXTRACT__LOAD_SCHEMA",
                    "placeholder": "foo",
                    "documentation": "bar",
                }
            ],
        ],
        # Preserve custom yaml descriptions starting with pipe
        [
            [
                {
                    "name": "add_metadata_columns",
                    "description": "My custom formatted description.\n Thats long.",
                    "label": "Add Metadata Columns",
                    "kind": "boolean",
                }
            ],
            [
                {
                    "name": "add_metadata_columns",
                    "description": "The tap description",
                    "label": "Add Metadata Columns",
                    "kind": "boolean",
                }
            ],
            [
                {
                    "name": "add_metadata_columns",
                    "description": "My custom formatted description.\n Thats long.",
                    "label": "Add Metadata Columns",
                    "kind": "boolean",
                }
            ],
        ],
        [
            [
                {
                    "name": "add_metadata_columns",
                    "description": "Nothing really",
                    "label": "Add Metadata Columns",
                    "kind": "boolean",
                }
            ],
            [
                {
                    "name": "add_metadata_columns",
                    "description": "the tap description.With some formatting issues. this one too.also this one.",
                    "label": "Add Metadata Columns",
                    "kind": "boolean",
                }
            ],
            [
                {
                    "name": "add_metadata_columns",
                    "description": "The tap description. With some formatting issues. This one too. Also this one.",
                    "label": "Add Metadata Columns",
                    "kind": "boolean",
                }
            ],
        ],
    ],
)
def test_merge_settings(existing, new, expected):
    utils = Utilities()
    merged_settings = utils._merge_settings(existing, new)
    assert merged_settings == expected


@pytest.mark.parametrize(
    "definition,expected",
    [
        pytest.param(
            {
                "name": "tap-mailchimp",
                "variant": "acarter24",
                "settings": [
                    {
                        "name": "dc",
                        "label": "Dc",
                    },
                ],
            },
            {
                "name": "tap-mailchimp",
                "variant": "acarter24",
                "settings": [
                    {
                        "name": "dc",
                        "label": "Data Center",
                    },
                ],
            },
            id="tap-mailchimp",
        ),
        pytest.param(
            {
                "name": "tap-totango",
                "variant": "edsoncezar16",
                "settings": [
                    {
                        "name": "api_url",
                        "options": [
                            {
                                "value": "https://api.totango.com",
                                "label": "Https://API Totango Com",
                            },
                            {
                                "value": "https://api-eu1.totango.com ",
                                "label": "Https://API Eu1 Totango Com ",
                            },
                        ],
                    },
                ],
            },
            {
                "name": "tap-totango",
                "variant": "edsoncezar16",
                "settings": [
                    {
                        "name": "api_url",
                        "options": [
                            {
                                "value": "https://api.totango.com",
                                "label": "US Endpoint",
                            },
                            {
                                "value": "https://api-eu1.totango.com",
                                "label": "EU Endpoint",
                            },
                        ],
                    },
                ],
            },
            id="tap-totango",
        ),
    ],
)
def test_apply_overrides(definition, expected):
    utils = Utilities()
    applied = utils._apply_overrides(definition)
    assert applied == expected
