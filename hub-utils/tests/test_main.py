import os
from unittest.mock import call, patch

import pytest

from hub_utils.main import S3, download_metadata

PATH = os.path.dirname(__file__)


@patch.object(S3, "download_latest")
def test_download_metadata(patch, monkeypatch: pytest.MonkeyPatch):
    expected_bucket = "TEST_BUCKET"
    monkeypatch.setenv("AWS_S3_BUCKET", expected_bucket)
    local_path = f"{PATH}/data/output_path"
    hub_yml_path = f"{PATH}/data/hub_data/_data/extractors/tap-csv/meltanolabs.yml"

    download_metadata(
        local_path,
        variant_path_list=hub_yml_path,
        all_sdk=False,
    )
    patch.assert_called_with(
        expected_bucket,
        "extractors/tap-csv/meltanolabs",
        f"{local_path}/extractors/tap-csv/meltanolabs.json",
    )


@patch.object(S3, "download_latest")
def test_download_metadata_ignore(patch, monkeypatch: pytest.MonkeyPatch):
    expected_bucket = "TEST_BUCKET"
    monkeypatch.setenv("AWS_S3_BUCKET", expected_bucket)
    local_path = f"{PATH}/data/output_path"
    monkeypatch.setenv("HUB_ROOT_PATH", PATH)
    download_metadata(
        local_path,
        # variant_path_list=hub_yml_path,
        all_sdk=True,
        ignore_list_str="extractors/tap-hubspot/hotgluexyz",
    )
    assert patch.call_count == 2
    patch.assert_has_calls(
        [
            call(
                expected_bucket,
                "extractors/tap-hubspot/meltanolabs",
                f"{local_path}/extractors/tap-hubspot/meltanolabs.json",
            ),
            call(
                expected_bucket,
                "extractors/tap-github/meltanolabs",
                f"{local_path}/extractors/tap-github/meltanolabs.json",
            ),
        ],
        any_order=True,
    )


@patch.object(S3, "download_latest")
def test_download_metadata_list(patch, monkeypatch: pytest.MonkeyPatch):
    expected_bucket = "TEST_BUCKET"
    monkeypatch.setenv("AWS_S3_BUCKET", expected_bucket)
    local_path = f"{PATH}/data/output_path"
    hub_yml_path = ",".join(
        [
            f"{PATH}/data/hub_data/_data/extractors/tap-csv/meltanolabs.yml",
            f"{PATH}/data/hub_data/_data/extractors/tap-cloudwatch/meltanolabs.yml",
        ]
    )

    download_metadata(
        local_path,
        variant_path_list=hub_yml_path,
        all_sdk=False,
    )
    patch.assert_has_calls(
        [
            call(
                expected_bucket,
                "extractors/tap-csv/meltanolabs",
                f"{local_path}/extractors/tap-csv/meltanolabs.json",
            ),
            call(
                expected_bucket,
                "extractors/tap-cloudwatch/meltanolabs",
                f"{local_path}/extractors/tap-cloudwatch/meltanolabs.json",
            ),
        ]
    )
