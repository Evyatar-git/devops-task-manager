variable "aws_region" {
  description = "AWS region for resources"
  type        = string
  default     = "us-east-1"
  
  validation {
    condition = contains([
      "us-east-1", "us-east-2", "us-west-1", "us-west-2",
      "eu-west-1", "eu-west-2", "eu-central-1"
    ], var.aws_region)
    error_message = "Region must be a valid AWS region."
  }
}

variable "project_name" {
  description = "Name of the project used for resource naming"
  type        = string
  default     = "devops-task-manager"
  
  validation {
    condition = can(regex("^[a-z][a-z0-9-]*[a-z0-9]$", var.project_name))
    error_message = "Project name must start with letter, contain only lowercase letters, numbers, and hyphens."
  }
}

variable "environment" {
  description = "Environment (dev, staging, prod)"
  type        = string
  default     = "dev"
  
  validation {
    condition = contains(["dev", "staging", "prod"], var.environment)
    error_message = "Environment must be dev, staging, or prod."
  }
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t3.micro"
  
  validation {
    condition = contains([
      "t3.micro", "t3.small", "t3.medium", "t3.large"
    ], var.instance_type)
    error_message = "Instance type must be a valid t3 instance type."
  }
}

variable "key_name" {
  description = "AWS Key Pair name for EC2 access"
  type        = string
  default     = "devops-task-manager-key"
  
  validation {
    condition = length(var.key_name) > 0
    error_message = "Key name cannot be empty."
  }
}