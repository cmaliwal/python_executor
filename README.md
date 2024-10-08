# Flask NSJail App

This project is a Flask API that securely runs Python scripts using NSJail.

## Requirements

- Docker
- Google Cloud SDK (for deployment)

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/cmaliwal/python_executor.git
    cd python_executor
    ```

2. Build the Flask application Docker image:

    ```bash
    docker build -t python-executor .
    ```

3. Run the application locally:

    ```bash
    docker run --privileged -p 8080:8080 python-executor
    ```

## Deploying to Google Cloud Run

1. Tag and push the Docker image to Google Container Registry:

    ```bash
    docker tag python-executor gcr.io/python-executor-434112/python-executor
    docker push gcr.io/python-executor-434112/python-executor
    ```

2. Deploy to Google Cloud Run:

    ```bash
    gcloud run deploy python-executor     --image gcr.io/python-executor-434112/python-executor     --platform managed     --region us-central1     --allow-unauthenticated
    ```

## Using the API

Once deployed, you can send a POST request to the `/execute` endpoint with your Python script to execute it securely.

Example requests:

### Example Request 1: Basic Arithmetic Operations

```json
{
    "script": "import json\n\ndef main():\n    result = {\n        \"status\": \"success\",\n        \"operation\": \"math_operations\",\n        \"data\": {\n            \"sum\": 10 + 5,\n            \"difference\": 10 - 5,\n            \"product\": 10 * 5,\n            \"quotient\": 10 / 5\n        }\n    }\n    return json.dumps(result)\n\nif __name__ == \"__main__\":\n    output = main()\n    print(output)"
}
```

### Example Request 2: List Processing

```json
{
    "script": "import json\n\ndef main():\n    numbers = [5, 10, 15, 20, 25]\n    result = {\n        \"status\": \"success\",\n        \"operation\": \"list_processing\",\n        \"data\": {\n            \"numbers\": numbers,\n            \"sum\": sum(numbers),\n            \"max_value\": max(numbers),\n            \"min_value\": min(numbers)\n        }\n    }\n    return json.dumps(result)\n\nif __name__ == \"__main__\":\n    output = main()\n    print(output)"
}
```

# API Documentation
For detailed information on the available API endpoints, request formats, and responses, please refer to the [API.md](./API.md) file.

# Assumptions:
The key assumptions made during the development of this project are documented in the [Assumptions.md](./Assumptions.md) file.

# Task List:
A detailed list of tasks and features implemented in this project can be found in the [task.md](./task.md) file.

# Future Scope of Improvements
There are potential future enhancements and features that could be added:

- **Authentication and Authorization**: Implement API key or OAuth2-based authentication to secure access.
- **Multi-Language Support**: Extend the API to support additional programming languages beyond Python.
- **Persistent Storage**: Introduce database integration to store execution results and provide an execution history feature.
- **Enhanced Logging and Monitoring**: Implement structured logging and integrate real-time monitoring tools.
- **CI/CD Pipeline**: Set up continuous integration and deployment processes to automate testing and deployment.
- **Web Interface**: Develop a user-friendly web interface for submitting and managing scripts directly from the browser.
