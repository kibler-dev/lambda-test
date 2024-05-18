terraform {
  cloud {
    organization = "{{TF_CLOUD_ORGANIZATION}}"

    workspaces {
      name = "{{TF_WORKSPACE}}"
    }
  }

  required_version = ">= 1.1.2"
}