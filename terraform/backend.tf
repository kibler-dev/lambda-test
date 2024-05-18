terraform {
  cloud {
    organization = "kibler-dev"

    workspaces {
      name = "lambda-test"
    }
  }

  required_version = ">= 1.1.2"
}