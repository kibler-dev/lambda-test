variable "aws_region" {
  description = "AWS region to create resources"
  default     = "us-west-2"
}

variable "lambda_function_name" {
  description = "Name of the Lambda function"
  default     = "hello-world-lambda"
}

variable "aws_assume_role_arn" {
  description = "ARN of the role to assume when creating resources"
  default     = ""
}

variable "aws_web_identity_token_file" {
  description = "OIDC token file to use when assuming the role"
  default     = ""
}
