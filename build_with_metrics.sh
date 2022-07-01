#! /bin/bash

# Run a jekyll build in netlify, but grab metrics stored in s3 first

curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" 
unzip -q awscliv2.zip 
./aws/install -i ~/aws-cli -b ~/aws-cli/bin
mkdir ~/.aws
cat > ~/.aws/credentials <<EOL
[default]
region = $ENV_DEFAULT_REGION
aws_secret_access_key = $ENV_SECRET_ACCESS_KEY
aws_access_key_id = $ENV_ACCESS_KEY_ID
EOL
~/aws-cli/bin/aws s3 cp s3://prod-meltano-bucket-01/hub_metrics/metrics.yml ./_data/metrics.yml 
~/aws-cli/bin/aws s3 cp s3://prod-meltano-bucket-01/hub_metrics/audit.yml ./_data/audit.yml
bundle exec jekyll build --config _config.yml,_config_netlify.yml