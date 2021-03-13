from flask import Flask
from flask import jsonify
from flask import request
import json
app = Flask(__name__)

todos = [
    {"label": "My first task", "done": False},
    {"label": "My second task", "done": False}
    ]
@app.route('/todos', methods=['GET'])
def hello_world():
    global todos
    json_data = jsonify(todos)
    return json_data

@app.route('/todos', methods=['POST'])
def add_new_todo():
    global todos
    request_body = request.data
    decode_object = json.loads(request_body)
    todos+=[decode_object]
    json_data=jsonify(todos)
    return json_data

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    global todos
    todos.pop(position)
    json_data=jsonify(todos)
    return json_data

if __name__=='__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)