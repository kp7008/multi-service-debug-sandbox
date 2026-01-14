from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"}), 200

@app.route('/api/services', methods=['GET'])
def list_services():
    services = [
        {"name": "api-gateway", "port": 5000},
        {"name": "auth-service", "port": 5001},
        {"name": "user-service", "port": 5002},
        {"name": "payment-service", "port": 5003},
    ]
    return jsonify({"services": services}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)