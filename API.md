# API Documentation

This document provides details on the API endpoints, request formats, and responses for the Flask API project.

## Base URL
http://localhost:8080/

## Endpoints

### 1. Run Python Script
**Endpoint**: `/execute`

**Method**: `POST`

**Description**: Executes a Python script within a secure environment using `nsjail`.

**Request Format**:
- Content-Type: `application/json`
- Body:
  ```json
    {
    "script": "import json\n\ndef main():\n    result = {\n        \"status\": \"ok\",\n        \"message\": \"Test script executed successfully\",\n        \"data\": {\n            \"value1\": 123,\n            \"value2\": \"abc\",\n            \"value3\": [1, 2, 3]\n        }\n    }\n    return json.dumps(result)\n\nif __name__ == \"__main__\":\n    output = main()\n    print(output)"
    }

**Response Format**:
- Success:
    ```json
    {
        "status": "ok",
        "message": "Test script executed successfully",
        "data": {
            "value1": 123,
            "value2": "abc",
            "value3": [1, 2, 3]
        }
    }

- Error
    ```json
    {
    "output": "",
    "errors": "Error details here"
    }
