/*
* 
*
*/

################################
### CONFIGURE REQUIRED PATHS ###
################################

############################################
### STANDARD ENVIRONMENT DEFINITION      ###
### NO NEED TO MODIFY REMAINDER OF FILE  ###
############################################

output "env_summary" { value = module.env.summary }
module "env" {
  source               = "git::https://github.com/slalom-ggp/dataops-infra.git//catalog/aws/environment"
  name_prefix          = local.name_prefix
  aws_region           = local.aws_region
  aws_credentials_file = local.aws_credentials_file
  resource_tags        = local.resource_tags
}
