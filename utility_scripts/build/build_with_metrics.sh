#! /bin/bash

# Run a jekyll build in netlify, but grab metrics stored in s3 first

# Make errors fail the build
set -euxo pipefail

# install CLI
if ! command -v aws >/dev/null 2>&1; then
  curl https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip -o awscliv2.zip
  unzip -q awscliv2.zip
  ./aws/install -i ~/aws-cli -b ~/aws-cli/bin --update
fi

# HACK because netlify doesn't let us set these (see https://remysharp.com/2019/05/18/aws-inside-netlify)
mkdir -p ~/.aws
cat > ~/.aws/credentials <<EOL
[default]
region = $ENV_DEFAULT_REGION
aws_secret_access_key = $ENV_SECRET_ACCESS_KEY
aws_access_key_id = $ENV_ACCESS_KEY_ID
EOL

# Grab files
~/aws-cli/bin/aws s3 cp s3://hub-metrics-b8ba2d5/prod/hub_metrics/variant_metrics.yml ./_data/variant_metrics.yml
~/aws-cli/bin/aws s3 cp s3://hub-metrics-b8ba2d5/prod/hub_metrics/audit.yml ./_data/audit.yml

gridsome build
