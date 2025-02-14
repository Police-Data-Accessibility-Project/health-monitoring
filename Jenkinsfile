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
                echo 'Running health checks...'
                sh 'python scripts/HealthMonitor.py'
                archiveArtifacts artifacts: 'health_monitoring.log', allowEmptyArchive: true
            }
        }
    }
    post {
        failure {
            script {
                def payload = """{
                    "content": "🚨 Build Failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}"
                }"""

                sh """
                curl -X POST -H "Content-Type: application/json" -d '${payload}' ${env.WEBHOOK_URL}
                """
            }
        }
    }
}