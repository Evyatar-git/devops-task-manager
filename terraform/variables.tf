variable "aws_region" {
  description = "AWS region for resources"
  type        = string
  default     = "us-east-1"  # Free tier friendly
}

variable "project_name" {
  description = "Name of the project"
  type        = string
  default     = "devops-task-manager"
}

variable "environment" {
  description = "Environment (dev, staging, prod)"
  type        = string
  default     = "dev"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t3.micro"  # Free tier eligible
}

variable "key_name" {
  description = "AWS Key Pair name for EC2 access"
  type        = string
  default     = ""  # We'll set this later
}