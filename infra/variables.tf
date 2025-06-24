variable "aws_region" {
  description = "AWS region"
  default     = "us-east-1"
}

variable "lambda_function_name" {
  default = "track_parcel"
}

variable "dynamodb_table_name" {
  default = "parcels"
}
