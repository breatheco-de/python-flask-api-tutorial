from flask import Flask
app = Flask(_name_)
from flask import Flask, jsonify
from flask import request

todos = [{ "label": "My first task", "done": False }]

@app.route("/todos", methods=["GET"])
def hello_world():
    json_text = jsonify(todos)
    return json_text

@app.route("/todos", methods=["POST"])
def add_new_todo():
    request_body = request.get_json(force=True)
    todos.append(request_body)
    print(todos)
    return jsonify(todos)

@app.route("/todos/<int:position>", methods=["DELETE"])
def delete_todo(position):
    todos.pop(position)
    print("This is the position to delete: ",position)
    return jsonify(todos)

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=3245, debug=True)