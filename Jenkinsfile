pipeline {
    agent any

    environment {
        IMAGE_NAME = 'cyber-clock-app'
        CONTAINER_NAME = 'cyber-clock-container'
        APP_PORT = '5000'
        HOST_PORT = '8081'
    }

    stages {

        stage('Build') {
            steps {
                echo '=== Building Docker Image ==='
                sh 'docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} .'
                sh 'docker tag ${IMAGE_NAME}:${BUILD_NUMBER} ${IMAGE_NAME}:latest'
            }
        }

        stage('Test') {
            steps {
                echo '=== Running Tests ==='
                sh '''
                    docker run --rm \
                        ${IMAGE_NAME}:latest \
                        sh -c "pip install pytest && pytest test_app.py -v"
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo '=== Deploying ==='
                sh 'docker stop ${CONTAINER_NAME} || true'
                sh 'docker rm   ${CONTAINER_NAME} || true'
                sh '''
                    docker run -d \
                        --name ${CONTAINER_NAME} \
                        -p ${HOST_PORT}:${APP_PORT} \
                        --restart unless-stopped \
                        ${IMAGE_NAME}:latest
                '''
                echo 'App running at http://localhost:8081'
            }
        }
    }

    post {
        success { echo '✅ Pipeline completed!' }
        failure { sh 'docker stop ${CONTAINER_NAME} || true' }
    }
}
