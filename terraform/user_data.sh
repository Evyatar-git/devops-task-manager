#!/bin/bash
yum update -y
yum install -y docker git

systemctl start docker
systemctl enable docker
usermod -a -G docker ec2-user

curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose

cd /home/ec2-user
git clone https://github.com/Evyatar-git/devops-task-manager.git
cd devops-task-manager

docker-compose build
docker-compose up -d

echo "Application deployed successfully!" > /var/log/user-data.log