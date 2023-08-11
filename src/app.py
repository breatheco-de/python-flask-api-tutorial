from flask import Flask
from flask import Flask, jsonify, request 
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False }
]
#GET
@app.route('/todos', methods=['GET'])
def hello_world():
    return  jsonify(todos)

#POST
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)
    todos.append(request_body)
    return jsonify(todos)

#DELETE
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    todos.pop((position-1))
    
    return jsonify(todos)

#
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)