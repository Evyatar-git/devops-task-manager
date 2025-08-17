FROM jenkins/jenkins:lts

USER root

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    python3-full \
    docker.io \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN usermod -aG docker jenkins
RUN chmod 666 /var/run/docker.sock || true

USER jenkins

RUN jenkins-plugin-cli --plugins "docker-workflow:521.v1a_a_dd2073b_2e"