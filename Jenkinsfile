pipeline {
  agent any
  stages {
    stage('validation_step') {
      steps {
        sh 'python3 ./module/validation.py'
      }
    }
    stage('next_step') {
      steps {
        sh 'python3 --version'
      }
    }
  }
}