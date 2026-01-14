from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"}), 200

@app.route('/verify/<user_id>', methods=['GET'])
def verify(user_id):
    return jsonify({"authenticated": True}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)