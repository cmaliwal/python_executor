# Assumptions

This document outlines the key assumptions made during the development of this Flask API project.

## General Assumptions
1. **Environment**: The application is designed to run in a Docker container, ensuring consistent behavior across different environments.
2. **Python Version**: The project assumes the use of Python 3.10, which is installed in the Docker container.
3. **Dependencies**: All dependencies are listed in `requirements.txt` and are assumed to be correctly installed within the container.
4. **Port Configuration**: The Flask API listens on port 8080 inside the container, and it's assumed that this port is available for use on the host machine.
5. **Security**: The API is secured using `nsjail` to run potentially unsafe Python scripts. It is assumed that `nsjail` is correctly configured and available in the system's `PATH`.

## Application-Specific Assumptions
1. **Script Input**: The API expects Python scripts to be provided in a specific JSON format via POST requests.
2. **Resource Limits**: It is assumed that `nsjail` is correctly limiting resources (CPU, memory, etc.) as configured in `nsjail.cfg`.
3. **Error Handling**: Basic error handling is implemented, but it is assumed that the API will be called with valid data under normal circumstances.
4. **Network Access**: The application assumes that no external network access is required by the Python scripts executed within the jail.

## Deployment Assumptions
1. **Google Cloud Run**: The application is assumed to be deployed on Google Cloud Run, with all necessary configurations for public access.
2. **External Dependencies**: The Docker image is self-contained, with no external dependencies required during runtime, apart from those defined in the Dockerfile.
