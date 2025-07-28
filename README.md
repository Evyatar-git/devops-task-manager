# DevOps Task Manager

A cloud-native task management application demonstrating modern DevOps practices including containerization, infrastructure as code, and automated deployment.

## Architecture

- **Application**: Python Flask with SQLite database
- **Containerization**: Docker with Docker Compose
- **Infrastructure**: AWS (VPC, ALB, Auto Scaling) managed with Terraform
- **Deployment**: Automated via user data scripts and container orchestration

## Features

- Task CRUD operations with persistent storage
- RESTful API endpoints
- Container-based deployment
- Health monitoring endpoints
- Auto-scaling AWS infrastructure
- Bootstrap responsive UI

## Technology Stack

- **Backend**: Python 3.11, Flask, SQLAlchemy
- **Frontend**: Bootstrap 5, Jinja2 templates
- **Database**: SQLite (development), scalable to RDS
- **Infrastructure**: Terraform, AWS (VPC, ALB, ASG, EC2)
- **Containerization**: Docker, Docker Compose

## Quick Start

### Local Development
```bash
git clone https://github.com/Evyatar-git/devops-task-manager.git
cd devops-task-manager
python -m venv venv && source venv/Scripts/activate  # Windows
pip install -r requirements.txt
python app.py
```
Visit http://localhost:5000

### Docker Development
```bash
docker-compose up
```
Visit http://localhost:5000

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/` | Main task list interface |
| GET    | `/add` | Add task form |
| POST   | `/add` | Create new task |
| GET    | `/complete/<id>` | Mark task as complete |
| GET    | `/delete/<id>` | Delete task |
| GET    | `/health` | Health check endpoint |

## AWS Infrastructure

### Infrastructure Components
- Multi-AZ VPC with public subnets
- Application Load Balancer with health checks
- Auto Scaling Group (1-2 t3.micro instances)
- Security groups with least-privilege access
- Launch templates with automated deployment

### Prerequisites
- AWS CLI configured with IAM user credentials
- Terraform >= 1.0
- EC2 key pair created

### AWS Setup (One-time)

**IAM User Setup:**
Create an IAM user with programmatic access and attach these policies:
- `AmazonEC2FullAccess`
- `AmazonVPCFullAccess` 
- `ElasticLoadBalancingFullAccess`
- `IAMReadOnlyAccess`

**EC2 Key Pair:**
Create a key pair named `devops-task-manager-key` in the AWS Console.

**AWS CLI Configuration:**
```bash
aws configure
aws sts get-caller-identity  # Verify setup
```

### Deploy to AWS
```bash
cd terraform
terraform init
terraform plan
terraform apply
```

### Access Application
```bash
terraform output load_balancer_url
```

**Note**: Allow 3-5 minutes after deployment for application initialization.

### Cleanup
```bash
terraform destroy
```

## Development

### Testing
```bash
python -m pytest tests/
```

### Infrastructure Changes
```bash
cd terraform
terraform plan    # Review changes
terraform apply   # Apply changes
```

### Project Structure
```
devops-task-manager/
├── app/                    # Flask application
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   └── templates/
│       ├── base.html
│       ├── index.html
│       └── add_task.html
├── terraform/              # Infrastructure as Code
│   ├── main.tf
│   ├── variables.tf
│   ├── security.tf
│   ├── compute.tf
│   ├── outputs.tf
│   ├── user_data.sh
│   └── terraform.tfvars
├── tests/                  # Application tests
│   └── test_app.py
├── app.py                  # Application entry point
├── config.py               # Configuration management
├── requirements.txt        # Python dependencies
├── Dockerfile
├── docker-compose.yml
├── .dockerignore           # Docker build exclusions
├── .gitignore              # Git exclusions
└── README.md
```

## Security Considerations

- IAM roles with least-privilege access
- Security groups restricting network access to required ports only
- Environment-based configuration management
- No hardcoded credentials in source code
- SSH access restricted (production deployment should limit to specific IPs)

## Cost Optimization

This project uses AWS free tier eligible resources:
- t3.micro EC2 instances (750 hours/month free)
- Application Load Balancer (750 hours/month free)
- VPC and networking components (no additional cost)

## Monitoring

- Application health checks at `/health` endpoint
- Load balancer health monitoring with automatic failover
- Auto Scaling based on instance health
- CloudWatch integration for metrics and logging

## Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/new-feature`)
3. Commit changes (`git commit -am 'Add new feature'`)
4. Push to branch (`git push origin feature/new-feature`)
5. Create Pull Request