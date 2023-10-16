import os
from unittest.mock import patch, call
from hub_utils.main import download_metadata, S3


PATH = os.path.dirname(__file__)


@patch.object(S3, "download_latest")
def test_download_metadata(patch):

    expected_bucket = "TEST_BUCKET"
    os.environ["AWS_S3_BUCKET"] = expected_bucket
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
        f"{local_path}/extractors/tap-csv/meltanolabs.json"
    )

@patch.object(S3, "download_latest")
def test_download_metadata_list(patch):

    expected_bucket = "TEST_BUCKET"
    os.environ["AWS_S3_BUCKET"] = expected_bucket
    local_path = f"{PATH}/data/output_path"
    hub_yml_path = ",".join([
        f"{PATH}/data/hub_data/_data/extractors/tap-csv/meltanolabs.yml",
        f"{PATH}/data/hub_data/_data/extractors/tap-cloudwatch/meltanolabs.yml",
    ])

    download_metadata(
        local_path,
        variant_path_list=hub_yml_path,
        all_sdk=False,
    )
    patch.assert_has_calls([
        call(
            expected_bucket,
            "extractors/tap-csv/meltanolabs",
            f"{local_path}/extractors/tap-csv/meltanolabs.json"
        ),
        call(
            expected_bucket,
            "extractors/tap-cloudwatch/meltanolabs",
            f"{local_path}/extractors/tap-cloudwatch/meltanolabs.json"
        )
    ])
