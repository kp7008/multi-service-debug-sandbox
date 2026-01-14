from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"}), 200

@app.route('/users', methods=['GET'])
def list_users():
    return jsonify({"users": []}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)