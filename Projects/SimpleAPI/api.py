from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# Simulated database
data_store = {
    1: {"name": "Alice", "role": "Developer"},
    2: {"name": "Bob", "role": "Manager"},
    3: {"name": "Charlie", "role": "Designer"},
}

# ✅ GET: Retrieve all users
@app.route('/programs', methods=['GET'])
def get_users():
    return jsonify(data_store), 200

# ✅ GET: Retrieve all users
@app.route('/contest', methods=['GET'])
def get_contest():
    return jsonify(data_store), 200

# ✅ GET: Retrieve a specific user
@app.route('/programs/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = data_store.get(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

# ✅ POST: Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user_id = max(data_store.keys(), default=0) + 1
    data_store[user_id] = data

    # Connect to local service using API Gateway [127.0.0.1:9090, 127.0.0.1:9091, 127.0.0.1:9092]
    # wait till the response is received
    return jsonify({"message": "User created", "id": user_id}), 201

# ✅ PUT: Update a user (Replace all fields)
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id in data_store:
        data_store[user_id] = request.json
        return jsonify({"message": "User updated"}), 200
    return jsonify({"error": "User not found"}), 404

# ✅ PATCH: Update specific fields
@app.route('/users/<int:user_id>', methods=['PATCH'])
def patch_user(user_id):
    if user_id in data_store:
        data_store[user_id].update(request.json)
        return jsonify({"message": "User partially updated"}), 200
    return jsonify({"error": "User not found"}), 404

# ✅ DELETE: Remove a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in data_store:
        del data_store[user_id]
        return jsonify({"message": "User deleted"}), 200
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(port= 8060, debug=True)
