pipeline {
  agent any
  stages {
    stage('build docker') {
      steps {
        sh 'docker build .'
      }
    }

    stage('run') {
      steps {
        sh 'docker-compose up'
      }
    }

    stage('test e2e') {
      steps {
        sh 'python e2e.py'
      }
    }

    stage('finish') {
      steps {
        sh 'docker stop (id)'
      }
    }

  }
}