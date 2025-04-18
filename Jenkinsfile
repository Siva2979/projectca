pipeline {
    agent any

    environment {
        IMAGE_NAME = 'digit-classifier'
        CONTAINER_NAME = 'digit-container'
    }

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/Siva2979/projectca.git'
            }
        }

        stage('Install Python & Train Model') {
            steps {
                script {
                    if (isUnix()) {
                        // Unix-based system commands
                        sh '''
                        python3 -m venv venv
                        source venv/bin/activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                        python app/train.py
                        '''
                    } else {
                        // Windows-based system commands
                        bat '''
                        python -m venv venv
                        .\\venv\\Scripts\\activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                        python app\\train.py
                        '''
                    }
                }
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
                script {
                    if (isUnix()) {
                        // Unix-based system command
                        sh """
                        docker rm -f ${CONTAINER_NAME} || true
                        """
                    } else {
                        // Windows-based system command
                        bat """
                        docker rm -f ${CONTAINER_NAME} || true
                        """
                    }
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    if (isUnix()) {
                        // Unix-based system command
                        sh """
                        docker run -d -p 5000:5000 --name ${CONTAINER_NAME} ${IMAGE_NAME}
                        """
                    } else {
                        // Windows-based system command
                        bat """
                        docker run -d -p 5000:5000 --name ${CONTAINER_NAME} ${IMAGE_NAME}
                        """
                    }
                }
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
