# `08` Delete todo

Deleting a todo is basically the opposite of adding a new one, so you should use 90% of the code from the `POST /todos` feature.

The main difference is that `DELETE /todos/<position:int>` will receive the position to delete in the URL of the request like this:

```python
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    return 'something'
```

When you use the `<` and `>` symbols, Flask will return whatever the client specified on that part of the URL as a variable.

For example:

```txt
The request DELETE /todos/1 will call the function 'delete_todo' with the variable 'position == 1'
The request DELETE /todos/323 will call the function 'delete_todo' with the variable 'position == 323'
```

## 📝 Instructions:

1. Add this endpoint to your `app.py` file.
