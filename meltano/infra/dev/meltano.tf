/*
* 
*
*/


output "meltano_summary" { value = module.meltano.summary }
module "meltano" {
  source               = "../../../../dataops-infra/catalog/aws/meltano"
  # TODO: Revert to git source after testing:
  # source             = "git::https://github.com/dataops-tk/dataops-infra.git//catalog/aws/meltano?ref=feature/meltano-module"

  environment          = module.aws_environ.environment
  name_prefix          = local.name_prefix
  resource_tags        = local.resource_tags
  project_source       = "git+https://${local.meltano_project_repo}.git"

  # TODO: Remove
  taps = {}
  data_lake_metadata_path = null
  # env                  = {
  #   GIT_URL = "git+https://gitlab.com/meltano/singerhub"
  #   GIT_PATH = "meltano-project"
  # }
}
