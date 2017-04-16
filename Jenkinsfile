pipeline {
    agent { label 'docker' }
    environment {
        IMAGE_NAME = "pdahlstrom/flask-docker-example:${env.BUILD_NUMBER}"
        REGISTRY_URL = 'https://index.docker.io/v1/'
        REGISTRY_CREDENTIALSID = 'docker-registry-pdahlstrom'
    }

    stages{
        stage('Run tests') {
            //agent { dockerfile true }

            steps {
                sh 'echo "Run tests"'
                sh 'python --version'
            }
        }

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
            when {
                branch 'master'
            }

            agent { 
                docker { image 'identt/rancher-compose:0.12.4' }
            }

            environment {
                RANCHER_URL = 'http://109.74.14.162:8080/'
                RANCHER_ACCESS_KEY = credentials('RANCHER_ACCESS_KEY')
                RANCHER_SECRET_KEY = credentials('RANCHER_SECRET_KEY')
                COMPOSE_PROJECT_NAME = 'flask-docker-example'
            }

            steps {
                sh 'rancher-compose --verbose up --upgrade --force-upgrade --pull -d --confirm-upgrade'
            }
        }
    }
}