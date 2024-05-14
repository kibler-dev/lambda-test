variable "aws_region" {
  description = "AWS region to create resources"
  default     = "us-west-2"
}

variable "lambda_function_name" {
  description = "Name of the Lambda function"
  default     = "hello-world-lambda"
}
