#!/usr/bin/env groovy

/*
This script runs all health monitoring actions
*/

pipeline {

    agent {
        dockerfile {
            filename 'Dockerfile'
            args '-e WEBHOOK_URL=$WEBHOOK_URL'
        }
    }

    stages {
        stage('Run health checks') {
            steps {
                sh 'exit 1'  // Simulate a failure
            }
        }
    }
    post {
        failure {
            script {
                def payload = """{
                    "content": "🚨 Build Failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                }"""

                sh """
                curl -X POST -H "Content-Type: application/json" -d '${payload}' ${env.WEBHOOK_URL}
                """
            }
        }
    }
}