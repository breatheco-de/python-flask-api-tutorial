## `07` POST /todos (add a new task)

Now that the method to GET `/todos` is done, we have to think about the rest of the endpoints in our API:

```txt
GET /todos
POST /todos
DELETE /todos
```

In order to build the `POST /todos` have do something similar that we did on the first endpoint. Remember that each endpoint in a Flask API is represented by a function and a decorator like this:

```python
@app.route('/blabla', methods=['GET'])
def hello_world():
    return 'Hello, World!'
```

Only in this case, we are not going to be expecting a GET request.

Also, we are expecting to receive the TODO that the client wants to add inside of the request body.

```python
from flask import request

# the request body is already json decoded and it comes in the request.data variable
print(request.data)
```

## 📝 Instructions

Add the folowing endpoint to your app.py and test it:

```python
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    print("Incoming request with the following body", request_body)
    return 'Response for the POST todo'
```

Remember to import request at the top of the file:

```python
from flask import request
```