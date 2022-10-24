
/* Requires the Docker Pipeline plugin */
// pipeline {
//     agent { docker { image 'python:3.10.7-alpine' } }
//     stages {
//         stage('build') {
//             steps {
//                 //sh 'python --version'
//                 sh 'node --version'
//                 sh 'node app.js'
//             }
//         }
//     }
// }

pipeline {
  agent { docker { image 'node:16.13.1-alpine' } }
  stages {
    stage('build') {
      steps {
            sh 'npm config ls'
            sh 'node --version'
            sh 'node app.js'
      }
    }
  }
}