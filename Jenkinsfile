pipeline {
    agent any

    environment {
        IMAGE_NAME = 'digit-classifier'
        CONTAINER_NAME = 'digit-container'
    }

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/Siva2979/projectca.git'
'
            }
        }

        stage('Install Python & Train Model') {
            steps {
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                python app/train.py
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${IMAGE_NAME}")
                }
            }
        }

        stage('Stop Old Container') {
            steps {
                sh """
                docker rm -f ${CONTAINER_NAME} || true
                """
            }
        }

        stage('Run Docker Container') {
            steps {
                sh """
                docker run -d -p 5000:5000 --name ${CONTAINER_NAME} ${IMAGE_NAME}
                """
            }
        }
    }

    post {
        success {
            echo "Deployment Successful! API running on port 5000."
        }
        failure {
            echo "Something went wrong. Check the logs."
        }
    }
}
