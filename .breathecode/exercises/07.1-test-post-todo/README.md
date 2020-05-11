## `07.1` Test your endpoint

This is what you have so far about the `POST /todos` endpoint, take some time to analyze each line:

```python
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    print("Incoming request with the following body", request_body)
    return 'Response for the POST todo'
```

Use postman, postwoman or any other API Request Builder that you like to test your API, here is an example on how to do it with postwoman:
https://youtu.be/HEQ-pSgOVtY

|  |  |
| ------ | -------- |
| Method | Post |
| URL: | /todos |
| Request Body | `{ "done": true, "label": "Sample Todo 1" }` |

