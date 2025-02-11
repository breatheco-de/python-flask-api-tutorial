from flask import Flask,jsonify,request
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():

    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
   request_body = request.json
   todos.append(request_body)
   return todos


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
   # Aclaracion para Javier
   # Pongo el -1 por que como trabajo con indices no haya confusion a la hora de eliminar 
   position_to_remove = position - 1
   del todos[position_to_remove]
   return todos




if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)