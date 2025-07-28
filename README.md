# DevOps Task Manager

A cloud-native task management application demonstrating modern DevOps practices including containerization, infrastructure as code, and automated CI/CD deployment.

## Architecture

- **Application**: Python Flask with SQLite database
- **Containerization**: Docker with Docker Compose
- **Infrastructure**: AWS (VPC, ALB, Auto Scaling) managed with Terraform
- **CI/CD**: Jenkins containerized pipeline with automated testing and deployment
- **Deployment**: Automated via user data scripts and container orchestration

## Features

- Task CRUD operations with persistent storage
- RESTful API endpoints
- Container-based deployment
- Health monitoring endpoints
- Auto-scaling AWS infrastructure
- Bootstrap responsive UI
- Automated CI/CD pipeline with testing and building

## Technology Stack

- **Backend**: Python 3.11, Flask, SQLAlchemy
- **Frontend**: Bootstrap 5, Jinja2 templates
- **Database**: SQLite (development), scalable to RDS
- **Infrastructure**: Terraform, AWS (VPC, ALB, ASG, EC2)
- **Containerization**: Docker, Docker Compose
- **CI/CD**: Jenkins (containerized with Docker)
- **Testing**: pytest with automated test execution

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

## CI/CD Pipeline (Jenkins)

### Prerequisites
- Docker Desktop running
- Git repository with code

### Setup Jenkins Environment
```bash
cd jenkins
docker-compose up -d
```

### Access Jenkins
- **Jenkins UI**: http://localhost:8080
- **Initial setup**: Follow setup wizard and install suggested plugins
- **Credentials**: Create admin user during setup

### Configure CI/CD Pipeline
1. Create new Pipeline job in Jenkins
2. Configure to use GitHub repository
3. Set branch to monitor (e.g., `feature/ci-cd-pipeline` or `main`)
4. Pipeline will automatically:
   - Run tests on code changes
   - Build Docker images
   - Perform health checks
   - Clean up resources

### Stop Jenkins
```bash
cd jenkins
docker-compose down
```

### Pipeline Features
- Automated testing with pytest
- Docker image building and verification
- Multi-stage health checking
- Automatic cleanup and resource management
- Build status notifications

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/` | Main task list interface |
| GET    | `/add` | Add task form |
| POST   | `/add` | Create new task |
| GET    | `/complete/<id>` | Mark task as complete |
| GET    | `/delete/<id>` | Delete task |
| GET    | `/health` | Health check endpoint |
| GET    | `/health/detailed` | Detailed health check with database |

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
├── jenkins/                # CI/CD Infrastructure
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── README.md
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
├── Jenkinsfile             # CI/CD pipeline definition
└── README.md
```

## Security Considerations

- IAM roles with least-privilege access
- Security groups restricting network access to required ports only
- Environment-based configuration management
- No hardcoded credentials in source code
- SSH access restricted (production deployment should limit to specific IPs)
- Containerized CI/CD environment for isolation

## Cost Optimization

This project uses AWS free tier eligible resources:
- t3.micro EC2 instances (750 hours/month free)
- Application Load Balancer (750 hours/month free)
- VPC and networking components (no additional cost)

## Monitoring

- Application health checks at `/health` endpoint
- Detailed health checks with database connectivity testing
- Load balancer health monitoring with automatic failover
- Auto Scaling based on instance health
- CloudWatch integration for metrics and logging
- CI/CD pipeline status monitoring

## Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/new-feature`)
3. Commit changes (`git commit -am 'Add new feature'`)
4. Push to branch (`git push origin feature/new-feature`)
5. Create Pull Request