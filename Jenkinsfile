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
        stage('Checkout Source Code') { 
            steps { 
                checkout([$class: 'GitSCM', 
                branches: [[name: '*/master']], 
                extensions: [], 
                userRemoteConfigs: [[url: 'https://github.com/voa2000/demo-python-nginx-app.git']]])
            }
        }
        stage('Build Images'){
            steps {
                 sh '''
             #!/bin/bash
             docker build -t voa2000/nginx-demo:nginx$tag nginx/.
             docker build -t voa2000/nginx-demo:app-1$tag app-1/.
             docker build -t voa2000/nginx-demo:app-2$tag app-2/.
             docker images
         '''
            }
        }
        stage('Login to DockerHub') {
			steps {
				sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			}
		}
		stage('Push to DockerHub') {
        steps {
				sh '''
                #!/bin/bash
                    echo "###### Pushing Image images to DockerHub !! ######";
                    docker push voa2000/nginx-demo:nginx$tag
                    docker push voa2000/nginx-demo:app-1$tag
                    docker push voa2000/nginx-demo:app-2$tag
                    echo "###### Image Publish to DockerHub Complete!! ######";
                '''
			}
     }
 }
}
