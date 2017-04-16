pipeline {
    agent { dockerfile true }

    stages{
        stage('Build and publish Docker image') {
            steps {
                def app = docker.build 'pdahlstrom/flask-docker-example:${env.BUILD_NUMBER}'
                app.push 'latest'
            }
        }

        stage('Deploy') {
            steps {
                sh 'echo Deploy'
            }
        }
    }
}