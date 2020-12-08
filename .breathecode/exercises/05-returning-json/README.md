## `05` Returning JSON

REST APIs have to return data in JSON format, not HTML format.

You can use the [flask jsonify](https://flask.palletsprojects.com/en/1.1.x/api/#flask.json.jsonify) function to easily convert any of the basic data-types to JSON data like this:

```python
def hello_world():
    # suppose you have some information in a json variable
    some_data = { "name": "Bobby", "lastname": "Rixer" }

    # you can convert that variable into a json string like this
    json_text = flask.jsonify(some_data)

    # and then you can return it on the response body like this
    return json_text
```

If we apply this knowledge to our todo-list project we can create a global variable `todos` that will contain the list of todos like this:

```python
todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

```

## 📝Instructions

1. Create a global variable todos. Do not declare the variable inside any function, make sure to declare the varible anywhere at the global scope. Make sure the variable contains at least one task item inside with the following structure:

```python
{ "label": "My first task", "done": False }
```

2. Change the return statement of your `hello_world` method to make it return the jsonify version of the global todos.

