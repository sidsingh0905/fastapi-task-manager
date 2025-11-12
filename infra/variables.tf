###########################################
# Global Variables
###########################################

variable "region" {
  description = "AWS region where all resources will be created"
  type        = string
  default     = "ap-south-1"
}

###########################################
# VPC Variables
###########################################

variable "vpc_cidr" {
  description = "CIDR block for the VPC"
  type        = string
  default     = "10.0.0.0/16"
}

variable "public_subnet_cidrs" {
  description = "List of CIDR blocks for public subnets"
  type        = list(string)
  default     = ["10.0.1.0/24", "10.0.2.0/24"]
}

variable "private_subnet_cidrs" {
  description = "List of CIDR blocks for private subnets"
  type        = list(string)
  default     = ["10.0.3.0/24", "10.0.4.0/24"]
}

###########################################
# EKS Variables
###########################################

variable "cluster_name" {
  description = "EKS cluster name"
  type        = string
  default     = "fastapi-prod-cluster"
}

###########################################
# RDS Variables
###########################################

variable "db_name" {
  description = "Name of the PostgreSQL database"
  type        = string
  default     = "tasksdb"
}

variable "db_username" {
  description = "Master username for the database"
  type        = string
  default     = "taskuser"
}

variable "db_password" {
  description = "Master password for the database"
  type        = string
  sensitive   = true
}

###########################################
# Tags
###########################################

variable "project_name" {
  description = "Common tag for project identification"
  type        = string
  default     = "fastapi-task-manager"
}
