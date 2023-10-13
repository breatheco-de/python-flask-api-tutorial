from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def hello_world():
    return 'Hello, World!'


@app.route('/todos', methods=['GET'])
def todo_hello():
    response_body = jsonify(todos)
    return response_body


@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    response_body = jsonify(todos)
    print("Incoming request with the following body", request_body)
    print("lista de todos", todos)
    return response_body


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position);
    response_body = jsonify(todos)
    print("This is the position to delete: ",position)
    return response_body


todos = [{ "label": "My first task", "done": False }]


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
