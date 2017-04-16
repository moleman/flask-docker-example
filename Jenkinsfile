pipeline {
    agent { label 'docker' }
    environment {
        IMAGE_NAME = "pdahlstrom/flask-docker-example:${env.BUILD_NUMBER}"
        REGISTRY_URL = 'https://index.docker.io/v1/'
        REGISTRY_CREDENTIALSID = 'docker-registry-pdahlstrom'
    }

    stages{
        stage('Build Docker image') {
            steps {
                script {
                    docker.build("${IMAGE_NAME}")
                }
            }
        }
        stage('Publish Docker image') {
            steps {
                withDockerRegistry([url: "${REGISTRY_URL}", credentialsId: "${REGISTRY_CREDENTIALSID}"]) {
                    script {
                        docker.image("${IMAGE_NAME}").push('latest')
                    }
                }
            }
        }

        stage('Deploy') {
            agent { 
                docker { image 'identt/rancher-compose:0.12.4' }
            }
            steps {
                sh 'rancher-compose --version'
            }
        }
    }
}