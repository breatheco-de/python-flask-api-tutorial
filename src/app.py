from flask import Flask, jsonify, request

app = Flask(__name__)

# A list to store todo items, each represented as a dictionary with "label" and "done" fields
todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

# Route to retrieve the list of todos
@app.route('/todos', methods=['GET'])
def hello_world():
    # Convert the todos list to a JSON response format
    json_text = jsonify(todos)

    # Return the JSON response to the front-end
    return json_text

# Route to add a new todo item
@app.route('/todos', methods=['POST'])
def add_new_todo():
    # Get JSON data from the request body
    request_body = request.json
    
    # Append the new todo item to the todos list
    todos.append(request_body)
    
    # Return the updated todos list as a JSON response
    json_text = jsonify(todos)
    return json_text

# Route to delete a todo item at a specific position
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    # Remove the item at the specified position in the todos list
    todos.pop(position)
    
    # Return the updated todos list as a JSON response
    json_text = jsonify(todos)
    return json_text

# These two lines should always be at the end of your app.py file to start the Flask application
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
