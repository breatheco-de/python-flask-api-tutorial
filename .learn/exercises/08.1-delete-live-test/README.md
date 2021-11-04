## `08.1` Test your endpoint

This is what you have so far about the `DELETE /todos/<int:position>` endpoint, take some time to analyze each line:

```python
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    return 'something'
```
Use Postman, Insomnia or any other API Request Builder that you like to test your API.

|  |  |
| ------ | -------- |
| Method | DELETE |
| URL: | `/todos/<int:position>` |
| Request Body | empty |

