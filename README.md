DevOps Attendances Project
This project is a learning project for DevOps who want to learn how to build a continuous integration and continuous
deployment (CI/CD) pipeline for a simple web application.

Overview
This project uses a simple web application written in Python and Flask to demonstrate how to build
a CI/CD pipeline using Jenkins, Docker, and AWS EC2 instances.
The pipeline performs the following steps:

Builds a Docker image for the web application.
Runs automated tests on the Docker image.
Deploys the Docker image to the test EC2 instance.
Runs integration tests on the deployed application.
If integration tests are successful, deploys the Docker image to the production EC2 instance.
Files:

Dockerfile
The Dockerfile is used to build the Docker image for the web application. 
It specifies the base image, installs the required dependencies, and copies the application code into the container.

requirements.txt
The requirements.txt file lists the Python dependencies required by the web application. 
This file is used by the Dockerfile to install the dependencies in the container.

app.py
The app.py file contains the code for the web application. 
It is a simple Flask application that responds to HTTP requests with a greeting message.

Jenkinsfile
The Jenkinsfile defines the Jenkins pipeline for building, testing, and deploying the web application. 
It specifies the stages and steps of the pipeline, including building the Docker image, running tests, 
and deploying to the test and production EC2 instances.

Conclusion
This project provides a basic understanding of how to build a CI/CD pipeline using Jenkins, Docker, 
and AWS EC2 instances for a simple web application. DevOps professionals can use this project as a starting point 
to build more complex CI/CD pipelines for their own applications.
