from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False }
]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)  
    return jsonify(todos)  


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    position -= 1  
    if 0 <= position < len(todos):
        del todos[position]
        return jsonify(todos), 200
    else:
        return jsonify({"error": "Todo not found"}), 404



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
