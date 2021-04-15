from flask import Flask,jsonify,flash,request,json
app = Flask(__name__)


todos = [
    { "label": "My first task", "done": False }
    ]

@app.route('/todos', methods=['GET'])
def hello_world():
   # return '<h1>Hello!</h1>'
    

    # supongamos que tienes cierta información (some_data) en una variable json
    #some_data = { "name": "Bobby", "lastname": "Rixer" }

    # puedes convertir esa variable en un string json así
    json_text = jsonify(todos)

    # y luego puedes retorarla (return) en el response body así:
    return json_text



@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    decoded_object=json.loads(request_body)
    todos.append(decoded_object)
    #print("Incoming request with the following body", request_body)
    return jsonify(todos)
    #return 'Response for the POST todo'

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    #print("This is the position to delete: ",position)
    posit=guide.query.get(position)
    db.session.delete(posit)
    db.session.commit()

    return guide_schema.jsonify(todos)
    #return jsonify(todos)
# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)

