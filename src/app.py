from flask import Flask, request, jsonify
from flask import request

app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

todos = [ { "label": "My first task", "done": False } ]


@app.route('/todos', methods=['POST'])
def create_todo():
    data = request.get_json()
    todos.append(data)
    return jsonify(data), 201  



@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)