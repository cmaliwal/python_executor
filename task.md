# Task List

This document outlines the key tasks and features implemented in this Flask API project.

## Initial Setup
- [x] Set up a Python 3.10 environment.
- [x] Create a basic Flask API structure.
- [x] Configure `nsjail` for secure execution of Python scripts.

## Dockerization
- [x] Write a Dockerfile to containerize the Flask API.
- [x] Ensure `nsjail` and Python are correctly installed in the container.
- [x] Set up multi-stage builds for an optimized Docker image.

## API Development
- [x] Implement `/execute` endpoint for executing Python scripts.
- [x] Add error handling and validation for script execution.

## Testing
- [x] Test the API locally using `curl` and Postman.
- [x] Ensure all dependencies are correctly installed in the Docker container.
- [x] Handle common errors, such as missing `nsjail` or invalid scripts.

## Deployment
- [x] Push the Docker image to Google Container Registry.
- [x] Deploy the Flask API to Google Cloud Run.
- [x] Configure the service to be publicly accessible.

## Documentation
- [x] Write `Assumptions.md`.
- [x] Write `API.md`.
- [x] Write `task.md`.
- [x] Prepare a GitHub repository description.
- [x] Outline the future scope of improvements.
