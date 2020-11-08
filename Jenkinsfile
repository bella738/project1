pipeline {
  agent any
  stages {
    stage('run') {
      steps {
        sh 'docker-compose up -d'
      }
    }

    stage('test e2e') {
      steps {
        sh 'python e2e.py'
      }
    }

    stage('finish') {
      steps {
        sh 'docker-compose stop'
      }
    }

  }
}