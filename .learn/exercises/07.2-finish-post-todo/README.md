# `07.2` Finish the POST /todos

Now... if we want to finish the post, we have to perform these specific actions:

+ First make sure that you are converting the request body into a real python data structure, like a dictionary. We already used `request.json` for that, since we know that the request will be in format application/json. If that is not known, you may want to use `request.get_json(force=True)` to ignore the content type and treat it like json. 

+ Add the dictionary into the list of `todos`.

+ Return the new list of `todos`.

Your deco should look like this by now:

```python

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    print("Incoming request with the following body", request_body)
    return 'Response for the POST todo'

```

## 📝 Instructions:

1. Add the decoded request body into the `todos` list.

2. Return the jsonify list of updated `todos`.
