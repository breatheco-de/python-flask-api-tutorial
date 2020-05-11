from flask import Flask, jsonify
app = Flask(__name__)

todos = [{ "label": "Sample", "done": True }]

@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)