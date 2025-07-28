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
                script {
                    def app = docker.image("${DOCKER_IMAGE}")
                    app.withRun('-p 5001:5000') { container ->
                        sh 'sleep 10'
                        sh 'curl -f http://localhost:5001/health || exit 1'
                    }
                }
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