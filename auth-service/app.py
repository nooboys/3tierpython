from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    if data["username"] == "admin" and data["password"] == "admin":
        return jsonify({"token": "fake-jwt-token"})
    return jsonify({"error": "Invalid credentials"}), 401

@app.route("/validate", methods=["POST"])
def validate():
    token = request.json.get("token")
    if token == "fake-jwt-token":
        return jsonify({"status": "valid"})
    return jsonify({"status": "invalid"}), 403

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
