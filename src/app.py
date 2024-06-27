from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False }
]

@app.route('/todos', methods=['GET'])
def get_todos():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    
    # Agregar el nuevo todo a la lista
    todos.append(request_body)
    
  
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    
    # Eliminar la tarea en la posición dada
    if position < len(todos):
        todos.pop(position)
    else:
        return jsonify({"error": "Position out of range"}), 400
    
  
    return jsonify(todos)

if __name__ == '__main__':
    app.run(debug=True)
