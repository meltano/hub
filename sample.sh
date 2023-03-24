hub_root='/Users/pnadolny/Documents/Git/GitHub/meltano/hub'
json_output_path='/Users/pnadolny/Documents/Git/GitHub/pnadolny/hub-utils/data'
sdk_variants=$(poetry run hub_utils get-variant-names $hub_root)
poetry run hub_utils extract-metadata-v2 "${sdk_variants}" $json_output_path
echo "Uploading to S3..."
poetry run hub_utils translate "${sdk_variants}" $json_output_path
