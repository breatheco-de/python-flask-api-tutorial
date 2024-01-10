# `07.2` Finish the POST /todos

Your code should look like this by now:

```python
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    return 'Response for the POST todo'
```

Now... if we want to finish our `POST` method, we have to perform the following specific actions:

+ First: Make sure that you are converting the request body into a real Python data structure, like a dictionary. You can see that we already used `request.json` for that since we know the request will be in `application/json`. However, if that is not known, you may want to use `request.get_json(force=True)` to ignore the content type and treat it like json. 

+ Second: Add the dictionary into the list of `todos`.

+ Last: Return the new list of `todos`.

Currently, this endpoint is not adding anything new to our 'database' (the `todos` list). 

Let's complete our code so the endpoint can do its job - add a new task to the `todos` list.


## 📝 Instructions:

1. Add the contents of the decoded request body into the `todos` list.

2. Return the updated list `todos` to the front end. 

3. Do not forget to `jsonify` your return. Why is this necessary? Ask the instructor to discuss this with the class. 
