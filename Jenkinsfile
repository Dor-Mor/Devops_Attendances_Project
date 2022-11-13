pipeline {
environment {
registry = "dormor5/devops_project"
registryCredential = 'DokerHubToken'
dockerImage = ''
}
agent any
stages {

}
stage('Building our image') {
steps{
script {
dockerImage = docker.build registry + ":$BUILD_NUMBER"
}
}
}
stage('Deploy our image') {
steps{
script {
docker.withRegistry( '', DokerHubToken ) {
dockerImage.push()
}
}
}
}
stage('Cleaning up') {
steps{
sh "docker rmi $registry:$BUILD_NUMBER"
}
}
}
}
