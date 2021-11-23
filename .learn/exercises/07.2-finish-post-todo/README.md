# `07.2` Finish the POST /todos

Now... if we want to finish the post, we have to perform these specific actions:

+ First make sure that you are converting the request body into a real python data structure, like a dictionary. We already used `request.json` for that, since we know that the request will be in format application/json. If that is not known, you may want to use `request.get_json(force=True)` to ignore the content type and treat it like json. 

+ Add the dictionary into the list of `todos`.

+ Return the new list of `todos`.

Your code should look like this by now:

```python

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    return 'Response for the POST todo'

```

Obviously this endopint is currently not adding anything new to our 'database' (the `todo` list). 

Let's complete the code so the endpoint can do its job - add a new task to the `todos`.


## 📝 Instructions:

1. Add the contents of the decoded request body into the `todos` list.

2. Return the updated list `todos` to the front end. 

3. Do not forget to `jsonify` your return. Why is this necessary - discuss with the class. 
