# `07` POST /todos (add a new task)

Now that the method to GET `/todos` is done, we have to think about the rest of the endpoints in our API:

```txt
GET /todos
POST /todos
DELETE /todos
```

In order to build the `POST /todos` endpoint, we have to do something similar to what we did in the first endpoint with our GET method. Remember that each endpoint in a Flask API is represented by decorator and a function, like this:

```python
@app.route('/myroute', methods=['GET'])
def hello_world():
    return 'Hello World!'
```

In this case, we are not going to be expecting a `GET` request, but rather a `POST` request.

Also, we are expecting to receive the TODO that the client wants to add inside of the request body.

```python
from flask import request

# The request body is already JSON decoded, and it comes in the request.json variable
print(request.json)
```

## 📝 Instructions:

1. Add the following endpoint to your `app.py` and test it:

```python
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    return 'Response for the POST todo'
```

2. Remember to import `request` at the top of the file:

```python
from flask import request
```


