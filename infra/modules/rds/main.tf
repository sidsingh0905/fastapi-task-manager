resource "aws_db_subnet_group" "this" {
  name       = "fastapi-rds-subnet-group"
  subnet_ids = var.private_subnet_ids
  tags = { Name = "fastapi-rds-subnet-group" }
}

resource "aws_db_instance" "this" {
  identifier              = "fastapi-rds"
  engine                  = "postgres"
  instance_class           = "db.t3.micro"
  allocated_storage        = 20
  db_subnet_group_name     = aws_db_subnet_group.this.name
  vpc_security_group_ids   = []
  db_name                  = var.db_name
  username                 = var.db_username
  password                 = var.db_password
  skip_final_snapshot      = true
  publicly_accessible      = false
}
