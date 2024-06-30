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
                // No need to run the script explicitly, as the CMD in the Dockerfile will handle it
            }
        }
        stage('Consolidate Log') {
            steps {
                echo 'Consolidating health_monitoring.log...'
                script {
                    // Define the path for the consolidated log file
                    def consolidatedLogFile = 'consolidated_health_monitoring.log'

                    // Ensure the consolidated log file exists
                    sh "touch ${consolidatedLogFile}"

                    // Copy the log file from the container to the Jenkins workspace
                    sh 'docker cp $(docker ps -q -l):/usr/src/app/health_monitoring.log ./new_health_monitoring.log'

                    // Append the new log to the consolidated log file
                    sh "cat new_health_monitoring.log >> ${consolidatedLogFile}"

                    // Clean up the new log file
                    sh "rm new_health_monitoring.log"
                }
                // Archive the consolidated log file
                archiveArtifacts artifacts: 'consolidated_health_monitoring.log', allowEmptyArchive: true
            }
        }
    }
}