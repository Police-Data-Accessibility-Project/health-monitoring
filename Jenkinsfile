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
                sh 'python scripts/check_search_endpoint.py'
                archiveArtifacts artifacts: 'health_monitoring.log', allowEmptyArchive: true
            }
        }
    }
}