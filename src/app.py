from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    {"label": "My first task", "done": False}
]

# GET
@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

# POST
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos)

# DELETE
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if position < len(todos):
        todos.pop(position)
        return jsonify(todos)
    return jsonify({"error": "Invalid position"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)