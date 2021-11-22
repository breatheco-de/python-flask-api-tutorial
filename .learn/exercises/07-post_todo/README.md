# `07` POST /todos (add a new task)

Now that the method to GET `/todos` is done, we have to think about the rest of the endpoints in our API:

```txt
GET /todos
POST /todos
DELETE /todos
```

In order to build the `POST /todos` we have to do something similar to what we did in the first endpoint. Remember that each endpoint in a Flask API is represented by a function and a decorator like this:

```python
@app.route('/blahblah', methods=['GET'])
def hello_world():
    return 'Hello, World!'
```

Except in this case we are not going to be expecting a GET request.

Also, we are expecting to receive the TODO that the client wants to add inside of the request body.

```python
from flask import request

# the request body is already json decoded and it comes in the request.json variable
print(request.json)
```

## 📝 Instructions:

1. Add the folowing endpoint to your app.py and test it:

```python
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    return 'Response for the POST todo'
```

2. Remember to import request at the top of the file:

```python
from flask import request
```
