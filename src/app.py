from flask import Flask, jsonify
from flask import request

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
    return 'Response for the POST todo'

    
if __name__ == '__main__':
    app.run(debug=True)
