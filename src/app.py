from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def hello():
    return 'Hello, World!'


@app.route('/todos', methods=['GET'])
def hello_world():
    response_body = jsonify(todos)
    return response_body


@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    response_body = jsonify(todos)
    print("Incoming request with the following body", request_body)
    print("lista de todos ", todos)
    return response_body


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if len(todos) < position:
        response_body = {'message': 'No existe la tarea con la posicion solicitada'}
        return response_body, 416
    del todos[position - 1]
    response_body = {'message': 'Elemento borrado correctamente', 
                     'result': todos}
    print("This is the position to delete: ",position)
    return jsonify(todos), 200


todos = [{ "label": "My first task", "done": False }]


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
