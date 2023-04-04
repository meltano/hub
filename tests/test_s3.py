import os

import boto3
import pytest
from moto import mock_s3

from hub_utils.s3 import S3
import shutil

LOCAL_PATH = f"{os.path.dirname(__file__)}/data/output_path"

@pytest.fixture(autouse=True)
def local_cleanup():
    yield
    shutil.rmtree(LOCAL_PATH)


@mock_s3
def test_s3_download(local_cleanup):
    conn = boto3.resource("s3", region_name="us-east-1")
    conn.create_bucket(Bucket="mybucket")
    object = conn.Object("mybucket", "extractors/tap-csv/meltanolabs/80d42f584dc79284c6b0d4a9f73f360c--2023-03-23.json")
    content = b"{'foo': 'bar'}"
    object.put(Body=content)
    s3_obj = S3()
    s3_obj.download_latest(
        "mybucket",
        "extractors/tap-csv/meltanolabs",
        f"{LOCAL_PATH}/extractors/tap-csv/meltanolabs.json"
    )
    assert os.path.isfile(f"{LOCAL_PATH}/extractors/tap-csv/meltanolabs.json") 
