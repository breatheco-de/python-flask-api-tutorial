# `05` Returning JSON

REST APIs have to return data in JSON format, not HTML format.

You can use the [flask jsonify](https://flask.palletsprojects.com/en/3.0.x/api/#flask.json.jsonify) function to easily convert any of the basic data-types to JSON data, like this:

```python
# Add the jsonify method to your Flask import
from flask import Flask, jsonify

# Suppose you have your data in the variable named some_data
some_data = { "name": "Bobby", "lastname": "Rixer" }

@app.route('/myroute', methods=['GET'])
def hello_world():
    # You can convert that variable into a json string like this
    json_text = jsonify(some_data)

    # And then you can return it to the front end in the response body like this
    return json_text
```

If we apply this knowledge to our todo-list project, we can create a global variable named `todos` that will hold the list of todos like this:

```python
todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]
```

## 📝 Instructions:

1. Create a global variable called `todos`. Do not declare the variable inside any function. Declare the variable in the global scope and make sure the variable contains at least one task item (our task objects) inside with the following structure:

```python
[ { "label": "My first task", "done": False } ]
```

2. Change the function on the GET method's endpoint from string output so that it will return the jsonified version of the global variable `todos`.
