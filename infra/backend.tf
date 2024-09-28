terraform {
  backend "s3" {
    bucket = "lanchonete-lambdas-bucket"
    key    = "lanchonete-lambda-define-auth-challenge/terraform.tfstate"
    region = "us-east-1"
  }
}