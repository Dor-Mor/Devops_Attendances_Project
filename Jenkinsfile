node {   
    stage('Clone repository') {
        git credentialsId: 'Git-credentials', url: 'https://github.com/Dor-Mor/Devops_Attendances_Project'
    }
    
    stage('Build image') {
       dockerImage = docker.build("dormor5/devops_project:latest")
    }
    
 stage('Push image') {
        withDockerRegistry([ credentialsId: "DockerHub-credentials", url: "https://hub.docker.com/repository/docker/dormor5/devops_project" ]) {
        dockerImage.push()
        }
    }    
}
