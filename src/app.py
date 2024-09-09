from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    {"label": "My first task", "done": False},
    {"label": "My second task", "done": False}
]

# Endpoint GOT para obtener la lista de todos
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

# Añadir un nuevo todo
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json  # Decodifica el cuerpo de la solicitud en un diccionario
    print(request_body)
    todos.append(request_body)  # Agrega el nuevo TODO a la lista de todos
    return jsonify(todos)  

# Eliminar un todo por posición
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    try:
        todos.pop(position)  # Intenta eliminar el todo en la posición dada
        return jsonify(todos)
    except IndexError:
        # Maneja el error si la posición está fuera del rango de la lista
        return jsonify({"error": "Posición fuera de rango"}), 404

# Código para ejecutar la aplicación Flask
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
