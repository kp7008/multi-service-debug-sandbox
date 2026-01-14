import os
from flask import Flask, jsonify, request
from functools import wraps

app = Flask(__name__)

# Get API key from environment
API_KEY = os.getenv('API_KEY', 'dev-key-12345')

def require_api_key(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        key = request.headers.get('X-API-Key')
        if key != API_KEY:
            return jsonify({"error": "Unauthorized"}), 401
        return f(*args, **kwargs)
    return decorated

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"}), 200

@app.route('/api/ping', methods=['GET'])
@require_api_key
def ping():
    return jsonify({"message": "pong"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
