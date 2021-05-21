/*
* 
*
*/


output "meltano_summary" { value = module.meltano.summary }
module "meltano" {
  source               = "../../../../dataops-infra/catalog/aws/meltano"
  # TODO: Revert to git source after testing:
  # source             = "git::https://github.com/dataops-tk/dataops-infra.git//catalog/aws/meltano?ref=feature/meltano-module"

  environment          = module.env.environment
  name_prefix          = local.name_prefix
  resource_tags        = local.resource_tags
  project_source       = local.meltano_project_repo

  # Note: This may need to be updated to account for daylight savings
  tz_utc_offset        = -6

  # TODO: Remove
  data_lake_metadata_path = null
  meltano_yml_path        = "../../../meltano.yml"
  default_target          = "target-athena"

  # env                  = {
  #   GIT_URL = "git+https://gitlab.com/meltano/singerhub"
  #   GIT_PATH = "meltano-project"
  # }
}
