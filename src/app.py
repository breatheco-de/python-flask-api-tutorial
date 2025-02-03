# Add the jsonify method to your Flask import
from flask import Flask, jsonify, request

app = Flask(__name__)
# Suppose you have your data in the variable named todos

todos = [ 
    { "label": "my first task", "done": False },
  ]


@app.route('/todos', methods=['GET'])
def hello_world():
    # You can convert that variable into a json string like this
    json_text = jsonify(todos)

    # And then you can return it to the front end in the response body like this
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append (request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    del todos[position]
    print("This is the position to delete:", position)
    return jsonify(todos)

# These two lines should always be at the end of your app.py file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)