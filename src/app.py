from flask import Flask
app = Flask(__name__)

@app.route('/todos', methods=['GET'])
def hello_world():
    retur <h1>Hello!</h1>

    
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)