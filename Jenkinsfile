pipeline {
    agent { label 'docker' }

    stages{
        stage('Build and publish Docker image') {
            steps {
                withDockerRegistry([credentialsId: 'docker-registry-pdahlstrom']) {
                    script {
                        def app = docker.build "pdahlstrom/flask-docker-example:${env.BUILD_NUMBER}"
                        app.push 'latest'
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