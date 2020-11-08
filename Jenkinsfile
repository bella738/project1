pipeline {
  agent any
  stages {
    stage('run') {
      steps {
        sh 'docker-compose up -d'
      }
    }

    stage('test ') {
      steps {
        sh 'curl http://0.0.0.0:8000/'
      }
    }

    stage('finish') {
      steps {
        sh 'docker-compose stop'
      }
    }

  }
}