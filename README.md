# OpenX Intern Project

This repository contains the tasks and progress for the OpenX Internship project.

## Tasks Completed:

### 1. Setup Environment
- Installed necessary tools such as Docker, Helm, and Kubernetes.
- Initialized the project structure.

### 2. Backend Web App
- Created a backend web app using Flask.
- Implemented an API endpoint to convert Fahrenheit to Celsius.
- Dockerized the Flask application.

### 3. Helm Chart
- Created a Helm chart to deploy the Flask app in a Kubernetes environment.
- Configured automatic scaling based on CPU usage.
- Exposed the application through a configurable port.

### 4. Locust Performance Testing
- Implemented performance testing using Locust.
- Created a Docker image and Helm chart for running Locust on Kubernetes.
- Ran performance tests on the Kubernetes cluster.

## Tasks In Progress:

### 4. Locust Performance Testing (further part)
- Ran performance tests on the Kubernetes cluster.

### 1. Continuous Integration (CI)
- Building CI pipelines to automate linting, testing, and deployment processes.

### 2. TensorFlow Serving Integration
- Integrating TensorFlow Serving to serve a computational graph for converting Fahrenheit to Celsius.

## Files Structure:
- **Locust**: Contains files related to performance testing using Locust.
- **Temperature-app-chart**: Helm chart for deploying the Flask app in Kubernetes.
- **model**: Files related to TensorFlow Serving integration.
- **Dockerfile**: Dockerfile for building the Flask app image.
- **locustfile.py**: Python script for Locust performance testing.
- **MLOps - intern - interview tasks - 2024.pdf**: Document outlining the internship tasks.

## How to Run:
1. Ensure Docker, Helm, and Kubernetes are installed.
2. Clone the repository: `git clone <repository_url>`
3. Navigate to the project directory.
4. Follow the instructions in each subdirectory to run specific components.

## Next Steps:
- Complete CI/CD setup.
- Integrate TensorFlow Serving.
- Perform comparative analysis of Flask and TensorFlow solutions.

