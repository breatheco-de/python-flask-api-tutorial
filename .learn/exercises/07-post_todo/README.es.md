## `07` POST /todos (añade un nuevo task)

Now that the method to GET `/todos` is done, we have to think about the rest of the endpoints in our API:

```txt
GET /todos
POST /todos
DELETE /todos
```

In order to build the `POST /todos` have do something similar that we did on the first enpoing, remember that each endpoint in a Flask API its represented by a function and a decorator like this:

```python
@app.route('/blabla', methods=['GET'])
def hello_world():
    return 'Hello, World!'
```

Only in this case we are not going to be expecting a GET request.

Also, we are expecting to receive the TODO that the client wants to add inside of the Request Body.