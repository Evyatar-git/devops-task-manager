#!/bin/bash
yum update -y
yum install -y docker git

# Start Docker
systemctl start docker
systemctl enable docker
usermod -a -G docker ec2-user

# Install Docker Compose
curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose

# Clone your repository (we'll update this with your actual repo)
cd /home/ec2-user
git clone https://github.com/Evyatar-git/devops-task-manager.git
cd devops-task-manager

# Build and run the application
docker-compose build
docker-compose up -d

# Set up log rotation
echo "Application deployed successfully!" > /var/log/user-data.log