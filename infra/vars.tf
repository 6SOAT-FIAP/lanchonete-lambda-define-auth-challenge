variable "aws_region" {
  description = "Região da AWS"
  type        = string
  default     = "us-east-1"
}

variable "lambda_function_name" {
  description = "Nome da função Lambda"
  default     = "lanchonete-lambda-define-auth-challenge"
}

variable "lambda_handler" {
  description = "Handler da função Lambda"
  default     = "lambda_function.lambda_handler"
}

variable "lambda_runtime" {
  description = "Ambiente de execução"
  default     = "python3.9"
}

variable "lambda_role" {
  description = "ARN da role IAM"
  default     = "arn:aws:iam::105971623004:role/LabRole"
}

variable "lambda_zip_path" {
  description = "Caminho do arquivo do pacote de implantação"
  default     = "../lambda_function.zip"
}