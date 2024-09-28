resource "aws_lambda_function" "lanchonete_lambda_auth" {
  function_name    = var.lambda_function_name
  handler          = var.lambda_handler
  runtime          = var.lambda_runtime
  role             = var.lambda_role
  filename         = var.lambda_zip_path
  source_code_hash = filebase64sha256(var.lambda_zip_path)
}