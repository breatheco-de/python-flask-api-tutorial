from flask import Flask
app = Flask(__name__)

@app.route('/todos', methods=['GET'])
def hello_world():
    return 'Hello!'

from flask import Flask,request,jsonify

app = Flask(__name__)

todos = [
    {
        "done": True,
        "label": "Sample Todo 1"
    },
    {
        "done": True,
        "label": "Sample Todo 2"
    }
]

@app.route("/todos", methods=['POST','GET'])
def all_todos():
    if request.method == 'POST':
        tarea = request.get_json()
        todos.append(tarea)
        return todos
    elif request.method == 'GET':
        return jsonify(todos)

   
@app.route("/todos/<int:index>", methods=['DELETE'])
def delete_todos(index):
    todos.pop(index)
    return jsonify(todos)

app.run()
























# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)