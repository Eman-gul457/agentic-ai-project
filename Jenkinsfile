pipeline {
    agent any

    environment {
        IMAGE_NAME = "agentic-ai-app"
        CONTAINER_NAME = "agentic-ai-container"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    credentialsId: 'github-creds',
                    url: 'https://github.com/Eman-gul457/agentic-ai-project.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t $IMAGE_NAME .
                '''
            }
        }

        stage('Stop Old Container') {
            steps {
                sh '''
                if [ "$(docker ps -aq -f name=$CONTAINER_NAME)" ]; then
                    docker stop $CONTAINER_NAME || true
                    docker rm $CONTAINER_NAME || true
                fi
                '''
            }
        }

        stage('Run New Container') {
            steps {
                sh '''
                docker run -d --name $CONTAINER_NAME -p 8000:8000 $IMAGE_NAME
                '''
            }
        }
    }

    post {
        success {
            echo "🚀 Deployment successful! Agentic AI is running on port 8000."
        }
        failure {
            echo "❌ Build failed. Check logs."
        }
    }
}
