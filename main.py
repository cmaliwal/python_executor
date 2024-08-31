import json
import os
import subprocess

from flask import Flask, jsonify, request

app = Flask(__name__)


def run_script(script):
    script_file = "/tmp/user_script.py"
    with open(script_file, "w") as f:
        f.write(script)

    try:
        result = subprocess.run(
            [
                "nsjail",
                "--quiet",
                "-Mo",
                "--chroot",
                "/",
                "--user",
                "65534",
                "--group",
                "65534",
                "--",
                "python3",
                script_file,
            ],
            check=True,
            capture_output=True,
            text=True,
            timeout=10,
        )

        return result.stdout

    except subprocess.CalledProcessError as e:
        return str(e), 400
    except subprocess.TimeoutExpired:
        return "Execution timeout", 400


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
