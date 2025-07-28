FROM jenkins/jenkins:lts

# Switch to root to install packages
USER root

# Install Python, pip, and Docker
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    python3-full \
    docker.io \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Add jenkins user to docker group and fix permissions
RUN usermod -aG docker jenkins
RUN chmod 666 /var/run/docker.sock || true

# Switch back to jenkins user
USER jenkins

# Install additional Jenkins plugins
RUN jenkins-plugin-cli --plugins "docker-workflow:521.v1a_a_dd2073b_2e"