pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/mahadevprsd7/loan-approval-pipeline.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t loan-jenkins-app .'
            }
        }
        stage('Run Docker Container') {
            steps {
                bat 'docker run -d -p 5000:5000 --name loan-container loan-jenins-app'
            }
        }
    }
}