import os
from pathlib import Path

import boto3


class S3:
    def __init__(self):
        self._client = self._create_client()

    def _create_client(self):
        aws_access_key_id = os.environ.get("AWS_ACCESS_KEY_ID")
        aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY")
        aws_session_token = os.environ.get("AWS_SESSION_TOKEN")
        aws_profile = os.environ.get("AWS_PROFILE")

        # AWS credentials based authentication
        if aws_access_key_id and aws_secret_access_key:
            aws_session = boto3.session.Session(
                aws_access_key_id=aws_access_key_id,
                aws_secret_access_key=aws_secret_access_key,
                aws_session_token=aws_session_token,
                # region_name=aws_region_name,
            )
        else:
            aws_session = boto3.session.Session(profile_name=aws_profile)
        s3 = aws_session.client("s3")
        return s3

    def hash_exists(self, s3_bucket, s3_file_path):
        components = s3_file_path.split("/")
        prefix = "/".join(components[:-1])
        file_name = components[-1]
        hash_id = file_name.split("--")[0]
        objs = self._client.list_objects_v2(Bucket=s3_bucket, Prefix=prefix).get(
            "Contents", []
        )
        existing_hashes = [os.path.basename(obj["Key"]).split("--")[0] for obj in objs]
        return hash_id in existing_hashes

    def upload(self, bucket, prefix, local_file_path):
        self._client.upload_file(local_file_path, bucket, prefix)

    def download_latest(self, bucket, prefix, local_file_path):
        objs = self._client.list_objects_v2(Bucket=bucket, Prefix=prefix).get(
            "Contents"
        )
        if not objs:
            return
        latest = sorted(
            [
                os.path.basename(obj["Key"]).replace(".json", "").split("--")[1]
                for obj in objs
            ]
        )[-1]
        latest_name = next(
            obj["Key"] for obj in objs if obj["Key"].endswith(f"{latest}.json")
        )
        Path(os.path.dirname(local_file_path)).mkdir(parents=True, exist_ok=True)
        self._client.download_file(bucket, latest_name, local_file_path)
