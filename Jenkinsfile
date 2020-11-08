pipeline {
  agent any
  stages {
    stage('run') {
      steps {
        sh 'docker-compose up -d'
      }
    }

    stage('test e2e') {
      parallel {
        stage('test e2e') {
          steps {
            sh 'python e2e.py'
          }
        }

        stage('Score') {
          steps {
            sh 'cat ./Score.txt'
          }
        }

      }
    }

    stage('finish') {
      steps {
        sh 'docker-compose stop'
      }
    }

  }
}