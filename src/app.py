
from flask import Flask
from flask import Flask, jsonify
from flask import request


todos = [{"label":"My first task", "done": False}]


app = Flask(__name__)
@app.route('/todos', methods=['GET'])
def show_todos():
    json_todo = jsonify(todos)
    return json_todo

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    return jsonify(todos)
















# These two lines should always be at the end of your app.py file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)