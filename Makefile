bundle:
	curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install -i ~/aws-cli -b ~/aws-cli/bin && \
    aws s3 cp s3://prod-meltano-bucket-01/hub_metrics/metrics.yml ./_data/metrics.yml && \
    aws s3 cp s3://prod-meltano-bucket-01/hub_metrics/audit.yml ./_data/audit.yml
	bundle exec jekyll build --config _config.yml,_config_netlify.yml