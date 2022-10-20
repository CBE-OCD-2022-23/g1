pipeline {
    agent any

    tools {
        // Install the Maven version configured as "M3" and add it to the path.
        maven "M3"
    }

    stages {
        stage('Build') {
            steps {
                // Get some code from a GitHub repository
                //git 'https://github.com/mery1233/Lab1-OCD'

                // Run Maven on a Unix agent.
                echo 'hello GitHub'

                sh 'pwd'

                sh 'python --version'
                

                // To run Maven on a Windows agent, use
                // bat "mvn -Dmaven.test.failure.ignore=true clean package"
            }

            }
    }
}