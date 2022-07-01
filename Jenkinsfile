pipeline { 
    agent any 
    options {
        skipStagesAfterUnstable()
    }
environment {
		DOCKERHUB_CREDENTIALS=credentials('DOCKER_HUB')
		tag           = "${env.BUILD_NUMBER}"
	}    
    stages {
        // stage('Checkout') { 
        //     steps { 
        //         checkout([$class: 'GitSCM', 
        //         branches: [[name: '*/master']], 
        //         extensions: [], 
        //         userRemoteConfigs: [[url: 'https://github.com/voa2000/demo-python-nginx-app.git']]])
        //     }
        // }
        stage('Build'){
            steps {
                 sh '''
             #!/bin/bash
             docker build -t voa2000/nginx-demo:$tag nginx/.
             docker images
         '''
            }
        }
        stage('Login') {
			steps {
				sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			}
		}
		stage('Push') {
        steps {
				sh 'docker push voa2000/nginx-demo:$tag'
			}
     }
 }
}
