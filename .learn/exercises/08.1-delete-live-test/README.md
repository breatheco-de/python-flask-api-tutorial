## `08.1` Test your endpoint

This is what you have so far about the `DELETE /todos/<int:position>` endpoint, take some time to analyze each line:

```python
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    return 'something'
```

Use postman, insomnia or any other API Request Builder that you like to test your API, here is an example on how to do it with postman:
https://youtu.be/HEQ-pSgOVtY

|  |  |
| ------ | -------- |
| Method | DELETE |
| URL: | `/todos/<int:position>` |
| Request Body | empty |

