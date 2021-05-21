/*
* 
*
*/

locals {
  root                 = "../.."                          # Path to root of repo
  secrets_folder       = "../../.secrets"                 # Default secrets location
  aws_credentials_file = "../../.secrets/aws-credentials" # AWS Credentials
  stage                = "dev"
  project_shortname    = "meltano-${local.stage}"
  aws_region           = "us-west-2"
  name_prefix          = "${local.project_shortname}-"
  meltano_project_repo = "gitlab.com/meltano/singerhub"
  meltano_project_dir  = "meltano"
  resource_tags = {
    project = local.project_shortname
    note    = "Managed by Terraform."
  }
}

terraform {
  required_providers {
    aws = "~> 3.0"
  }
}

provider "aws" {
  region                  = local.aws_region
  shared_credentials_file = local.aws_credentials_file
  profile                 = "default"
}
