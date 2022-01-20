# `05` Returning JSON

REST APIs have to return data in JSON format, not HTML format.

You can use the [flask jsonify](https://flask.palletsprojects.com/en/1.1.x/api/#flask.json.jsonify) function to easily convert any of the basic data-types to JSON data like this:

```python

# add the jsonify method to your Flask import
    from flask import Flask, jsonify

# suppose you have your data in the variable some_data
    some_data = { "name": "Bobby", "lastname": "Rixer" }

@app.route('/blahblah', methods=['GET'])
def hello_world():
    # you can convert that variable into a json string like this
    json_text = jsonify(some_data)

    # and then you can return it to the front end in the response body like this
    return json_text
```

If we apply this knowledge to our ToDo-list project we can create a global variable `todos` that will contain the list of todos like this:

```python
todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]
```

## 📝Instructions:

1. Create a global variable todos. Do not declare the variable inside any function, make sure to declare the variable anywhere at the global scope. Make sure the variable contains at least one task item inside with the following structure:

```python
[ { "label": "My first task", "done": False } ]
```

2.  Change the function that is executed on the GET method's endpoint to make it return the jsonified version of the global variable `todos`.
