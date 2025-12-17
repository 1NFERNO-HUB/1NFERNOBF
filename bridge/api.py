# bridge/api.py
from flask import Flask, request, jsonify
from core.pipeline import run_obfuscation_string

app = Flask(__name__)

@app.route('/obfuscate', methods=['POST'])
def handle_api():
    user_code = request.json.get('code')
    # Run the engine on the raw string
    protected_code = run_obfuscation_string(user_code)
    return jsonify({"result": protected_code})

def start_api():
    app.run(port=5000)
