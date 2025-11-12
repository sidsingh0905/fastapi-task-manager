terraform {
  backend "s3" {
    bucket         = "fastapi-todo-terraform-state" # 👈 Replace with your own unique bucket name
    key            = "prod/terraform.tfstate"
    region         = "ap-south-1"
    dynamodb_table = "fastApi-terraform-state-lock"
    encrypt        = true
  }
}
