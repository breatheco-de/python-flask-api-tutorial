## `07.2` Finish the POST /todos

Now... if we want to finish the post, we have to do two specific actions:

1. Decode the request.data to convert it into a real python dictionary.
2. Add the dictionary into the list of todos.
3. Return the new list of todos.

To decode any json string into a real python object, we can use this function:

```python
import json
decoded_object = json.loads(original_string)
```

## 📝 Instructions

1. Use the json.loads function to decode the request.data
2. Add the decoded object into the todos list.
3. Return the jsonify list of updated todos