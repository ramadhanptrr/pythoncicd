pipeline {
  agent any
  stages {
    stage('validation') {
      steps {
        sh 'python3 ./module/validation.py'
      }
    }
    stage('next_step') {
      steps {
        sh 'python3 print("hello")'
      }
    }
  }
}