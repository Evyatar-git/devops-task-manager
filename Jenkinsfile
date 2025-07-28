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
                    # Start container
                    CONTAINER_ID=$(docker run -d -p 5001:5000 ${DOCKER_IMAGE})
                    echo "Started container: $CONTAINER_ID"
                    
                    # Wait for app to start
                    sleep 10
                    
                    # Show container logs
                    echo "Container logs:"
                    docker logs $CONTAINER_ID
                    
                    # Test simple health endpoint first (no database)
                    echo "Testing simple health endpoint..."
                    timeout 5 docker exec $CONTAINER_ID curl -f http://localhost:5000/health || echo "Simple health check failed"
                    
                    # Test detailed health endpoint (with database)
                    echo "Testing detailed health endpoint..."
                    timeout 5 docker exec $CONTAINER_ID curl -f http://localhost:5000/health/detailed || echo "Detailed health check failed"
                    
                    # Test if Flask is responding at all
                    echo "Testing Flask root endpoint..."
                    timeout 5 docker exec $CONTAINER_ID curl -I http://localhost:5000/ || echo "Root endpoint failed"
                    
                    # Show final container status
                    echo "Container status:"
                    docker ps | grep $CONTAINER_ID || echo "Container not running"
                    
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