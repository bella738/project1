pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        sh 'sh docker-run-command.txt'
      }
    }

    stage('run') {
      steps {
        sh 'docker-compose up -d'
      }
    }

    stage('test') {
      steps {
        sh '''python e2e.py

'''
      }
    }

    stage('finishh') {
      steps {
        sh 'docker-compose stop'
      }
    }

  }
}