variable "cluster_name" {
  description = "EKS cluster name"
  type        = string
}

variable "vpc_id" {
  description = "VPC ID where the EKS cluster will be created"
  type        = string
}

variable "private_subnets" {
  description = "Private subnet IDs for the EKS worker nodes"
  type        = list(string)
}

variable "public_subnets" {
  description = "Public subnet IDs for the EKS cluster networking"
  type        = list(string)
}

variable "region" {
  description = "AWS region"
  type        = string
}
