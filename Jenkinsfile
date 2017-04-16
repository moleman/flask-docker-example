pipeline {
    agent { dockerfile true }

    stages{
        stage('Build and publish Docker image') {
            steps {
                docker.build('pdahlstrom/flask-docker-example:latest').push()
            }
        }

        stage('Deploy') {
            steps {
                sh 'echo Deploy'
            }
        }
    }
}