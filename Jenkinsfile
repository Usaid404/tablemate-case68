pipeline {
  agent any
  stages {
    stage('Checkout') { steps { checkout scm } }
    stage('Unit tests') { steps { sh 'python3 -m unittest discover -s tests -v 2> report.txt' } }
    stage('Docker build') { steps { sh 'docker build -t tablemate:${BUILD_NUMBER} .' } }
  }
  post {
    always  { archiveArtifacts artifacts: 'report.txt' }
    success { sh 'echo "TableMate build ${BUILD_NUMBER}: SUCCESS" > notify.txt' }
    failure { sh 'echo "TableMate build ${BUILD_NUMBER}: FAILED" > notify.txt' }
  }
}
