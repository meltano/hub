# Initial AWS setup

1. From the AWS web console:
   1. Create an S3 bucket and take note of the AWS region.
   2. Create an IAM account with web access disabled, api access enabled.
   3. Store the access key ID and secret access key in you password manager.

## Athena setup

1. From the AWS Athena web console:
   1. Edit the `primary` workgroup and set the query result location to `s3://<bucket>/athena/query_output/`
