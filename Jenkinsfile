pipeline {
  agent any
  stages {
    stage('run') {
      parallel {
        stage('run') {
          steps {
            sh 'docker-compose up -d'
          }
        }

        stage('open Score.txt') {
          steps {
            sh 'cat ./Score.txt'
          }
        }

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