import json
import os
import subprocess
import tempfile
from flask import Flask, jsonify, request

app = Flask(__name__)

def prepare_script(script):
    if "import json" not in script:
        script = "import json\n" + script

    if "main()" in script and "output = main()" not in script:
        if "print(main())" in script or "main()" in script.splitlines():
            script = script.replace("print(main())", "output = main()\n    print(output)")
            script = script.replace("main()", "output = main()\n    print(output)")
        else:
            script += "\n\nif __name__ == \"__main__\":\n    output = main()\n    print(output)"
    elif "if __name__ == \"__main__\":" not in script:
        script += "\n\nif __name__ == \"__main__\":\n    output = main()\n    print(output)"

    return script

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
            return None, result.stderr, None

        stdout_lines = result.stdout.strip().split("\n")
        stdout_capture = "\n".join(stdout_lines[:-1])
        main_output = stdout_lines[-1] if stdout_lines else ""

        return main_output, stdout_capture, None
    except subprocess.TimeoutExpired:
        os.remove(script_file)
        return None, None, "Execution timeout"

    finally:
        os.remove(script_file)

@app.route("/execute", methods=["POST"])
def execute():
    data = request.json
    script = data.get("script", "")

    if "def main()" not in script:
        return jsonify({"error": "No main() function found in the script."}), 400

    script = prepare_script(script)

    main_output, stdout_capture, error = run_script(script)

    if error:
        return jsonify({"error": error}), 400

    try:
        result = json.loads(main_output)
        return jsonify({"result": result, "stdout": stdout_capture})
    except json.JSONDecodeError as e:
        return jsonify({"error": "The main() function must return valid JSON."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
