pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        sh 'docker-compose up -d'
      }
    }

    stage('run') {
      steps {
        sh 'curl http://0.0.0.0:8777/'
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