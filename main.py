import json
import os
import subprocess
import tempfile
from flask import Flask, jsonify, request

app = Flask(__name__)

def run_script(script):
    with tempfile.NamedTemporaryFile(suffix=".py", delete=False) as temp_script:
        script_file = temp_script.name
        temp_script.write(script.encode())

    try:
        result = subprocess.run(
            ['nsjail', '--config', '/etc/nsjail/nsjail.cfg', '--', '/usr/local/bin/python3', script_file],
            capture_output=True, text=True, timeout=10
        )

        if result.returncode != 0:
            return result.stderr, 400

        return result.stdout

    except subprocess.TimeoutExpired:
        os.remove(script_file)
        return "Execution timeout", 400

    finally:
        os.remove(script_file)

@app.route("/execute", methods=["POST"])
def execute():
    data = request.json
    script = data.get("script", "")

    if "def main()" not in script:
        return jsonify({"error": "No main() function found in the script."}), 400

    try:
        output = run_script(script)
        result = json.loads(output)
        return jsonify(result)
    except json.JSONDecodeError:
        return jsonify({"error": "The main() function must return valid JSON."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
