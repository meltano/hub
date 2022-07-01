#! /bin/bash

# Run a jekyll build in netlify, but grab metrics stored in s3 first

# Make errors fail the build
set -euxo pipefail

# install CLI
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" 
unzip -q awscliv2.zip 
./aws/install -i ~/aws-cli -b ~/aws-cli/bin

# HACK because netlify doesn't let us set these (see https://remysharp.com/2019/05/18/aws-inside-netlify)
mkdir ~/.aws
cat > ~/.aws/credentials <<EOL
[default]
region = $ENV_DEFAULT_REGION
aws_secret_access_key = $ENV_SECRET_ACCESS_KEY
aws_access_key_id = $ENV_ACCESS_KEY_ID
EOL

# Grab files
~/aws-cli/bin/aws s3 cp s3://prod-meltano-bucket-01/hub_metrics/metrics.yml ./_data/metrics.yml 
~/aws-cli/bin/aws s3 cp s3://prod-meltano-bucket-01/hub_metrics/audit.yml ./_data/audit.yml

# Build site (doing the correct thing if we are in a deploy-preview (see https://github.com/meltano/hub/pull/626))
if [ -e _config_netlify.yml ]
then
    bundle exec jekyll build --config _config.yml,_config_netlify.yml
else
    bundle exec jekyll build --config _config.yml
fi
