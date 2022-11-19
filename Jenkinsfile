pipeline {
 agent any
    environment {
        gitHubCredential = 'Git_c'
        gitHubURL = 'https://github.com/Dor-Mor/Devops_Attendances_Project.git'
        dockerHubRegistry = 'dormor5/devops_project'
        dockerHubCredentials = 'DockerHub_c'
        image = ''
        prodIp = '172.31.5.244'
        testIp = '172.31.8.217'
    }
    stages {
        stage ('Checkout') {
            steps {
                echo "CHECKOUT --- START"
                checkout([  $class: 'GitSCM', 
                            branches: [[name: 'master']], 
                            doGenerateSubmoduleConfigurations: false, 
                            extensions: [[$class: 'CleanCheckout']], 
                            submoduleCfg: [], 
                            userRemoteConfigs: [[credentialsId: gitHubCredential,
                                                url: gitHubURL]]
                ])            
                echo "CHECKOUT --- SUCCESS"
            }
        }
	    stage ('Build') {
            steps {
                echo "BUILD --- START"
                script {
                    image = docker.build(dockerHubRegistry + ":latest",
                    ".")
                }
                echo "BUILD --- SUCCESS"
            }
        }
        stage ('Push to DockerHub') {
            steps {
                echo "PUSH TO DOCKERHUB --- START"
                script {
                    docker.withRegistry( '', dockerHubCredentials ) {
                        image.push()
                    }
                }
                echo "PUSH TO DOCKERHUB --- SUCCESS"
            }
        }
        stage ('Deploy&Test- Test Env') {
            steps {
                echo "DEPLOY TO TEST ENVIRONMENT --- START"
                sshagent (credentials: ['ssh-test']) {
                    sh '''
                        scp -o StrictHostKeyChecking=no ./docker-compose.yml ec2-user@${testIp}:/home/ec2-user
                        scp -o StrictHostKeyChecking=no ./env-mysql ec2-user@${testIp}:/home/ec2-user
                        ssh ec2-user@${testIp} -o BatchMode=yes -o StrictHostKeyChecking=no \
                        "docker-compose down && docker pull dormor5/devops_project && \
                        docker-compose up -d && sleep 15 && curl -I http://localhost:5000/"
                    '''
                }
                echo "DEPLOY TO TEST ENVIRONMENT --- SUCCESS"
            }
        }
        stage ('Deploy&Test- Prod Env') {
            steps {
                timeout (time: 180, unit: 'SECONDS') {
                    input (message: "Are you sure you want to deploy to production?",
                           ok: "Yes")
                }
                echo "DEPLOY TO PRODUCTION ENVIRONMENT --- START"
                sshagent (credentials: ['ssh-prod']) {
                    sh '''
                        scp -o StrictHostKeyChecking=no ./docker-compose.yml ec2-user@${prodIp}:/home/ec2-user
                        scp -o StrictHostKeyChecking=no ./env-mysql ec2-user@${prodIp}:/home/ec2-user
                        ssh ec2-user@${prodIp} -o BatchMode=yes -o StrictHostKeyChecking=no \
                        "docker-compose down && docker pull dormor5/devops_project && \
                        docker-compose up -d && sleep 15 && curl -I http://localhost:5000/"
                    '''
                }
                echo "DEPLOY TO PRODUCTION ENVIRONMENT --- SUCCESS"
            }
        }
    }
    post {
        always {
            echo "CLEAN WORKSPACE --- START"
            cleanWs()
            echo "CLEAN WORKSPACE --- SUCCESS"
        }
    }
}
