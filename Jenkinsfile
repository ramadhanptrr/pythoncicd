pipeline {
  agent any
  stages {
    stage('validation_step') {
      steps {
        sh 'python3 ./module/validation.py'
      }
    }
    stage('redshift_table_creation') {
      steps {
        sh 'python3 --version'
      }
    }
    stage('rds_config_insert') {
      steps {
        sh 'python3 --version'
      }
    }
    stage('copying_dag') {
      steps {
        sh 'python3 --version'
      }
    }
    stage('copy_sql_file') {
      steps {
        sh 'python3 --version'
      }
    }
  }
}