pipeline {
    agent any

    environment {
        PROJECT_NAME = "agentic-ai"
        IMAGE_NAME = "agentic-ai-app"
        CONTAINER_NAME = "agentic-ai-container"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git credentialsId: 'github-creds', url: 'https://github.com/Eman-gul457/agentic-ai-project.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install -r requirements.txt
                deactivate
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
                if [ $(docker ps -aq -f name=$CONTAINER_NAME | wc -l) -gt 0 ]; then
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
            echo "🚀 Deployment Successful!"
        }
        failure {
            echo "❌ Build Failed!"
        }
    }
}
      
