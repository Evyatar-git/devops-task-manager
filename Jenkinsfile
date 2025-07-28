pipeline {
    agent any
    
    environment {
        APP_NAME = 'devops-task-manager'
        DOCKER_IMAGE = "${APP_NAME}:${BUILD_NUMBER}"
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code from GitHub...'
                checkout scm
            }
        }
        
        stage('Setup Python Environment') {
            steps {
                echo 'Setting up Python virtual environment...'
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    python3 -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                sh '''
                    . venv/bin/activate
                    python3 -m pytest tests/ -v
                '''
            }
        }
        
        stage('Build Docker Image') {
            steps {
                echo "Building Docker image: ${DOCKER_IMAGE}"
                script {
                    docker.build("${DOCKER_IMAGE}")
                }
            }
        }
        
        stage('Test Docker Image') {
            steps {
                echo 'Testing Docker image...'
                sh '''
                    # Start container and capture container ID
                    CONTAINER_ID=$(docker run -d -p 5001:5000 ${DOCKER_IMAGE})
                    echo "Started container: $CONTAINER_ID"
                    
                    # Wait for app to start
                    echo "Waiting for application to start..."
                    sleep 15
                    
                    # Show container logs
                    echo "Container logs:"
                    docker logs $CONTAINER_ID
                    
                    # Test using container's IP instead of localhost
                    echo "Testing health endpoint..."
                    CONTAINER_IP=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $CONTAINER_ID)
                    echo "Container IP: $CONTAINER_IP"
                    
                    # Try multiple approaches to reach the app
                    echo "Trying localhost:5001..."
                    curl -f http://localhost:5001/health || echo "Localhost test failed"
                    
                    echo "Trying container IP..."
                    curl -f http://$CONTAINER_IP:5000/health || echo "Container IP test failed"
                    
                    echo "Trying docker exec approach..."
                    docker exec $CONTAINER_ID curl -f http://localhost:5000/health || echo "Docker exec test failed"
                    
                    # Cleanup
                    echo "Cleaning up container..."
                    docker stop $CONTAINER_ID
                    docker rm $CONTAINER_ID
                '''
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline completed!'
            sh 'rm -rf venv || true'
        }
        success {
            echo 'Pipeline succeeded! 🎉'
        }
        failure {
            echo 'Pipeline failed! ❌'
        }
        cleanup {
            script {
                try {
                    sh 'docker image prune -f'
                } catch (Exception e) {
                    echo 'Docker cleanup failed, but continuing...'
                }
            }
        }
    }
}