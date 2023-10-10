from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text


@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)
    todos.append(request_body)
    response_body = jsonify(todos)
    print("Incoming request with the following body", request_body)
    return response_body


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if len(todos) < position : 
        response_body = {"message": "Not found"}
        return response_body, 416
    del todos[position - 1]
    response_body = {"message": "Deleted element", 
                         "result": todos}
    print("This is the position to delete: ",position)
    return jsonify(todos), 200

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
