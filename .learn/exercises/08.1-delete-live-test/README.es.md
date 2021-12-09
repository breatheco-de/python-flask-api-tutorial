# `08.1` Test your endpoint

Hasta ahora esto es lo que tienes sobre el endpoint  `DELETE /todos/<int:position>`, tómate tu tiempo para analizar cada línea:

```python
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    return 'something'
```

Usa Postman, Insomnia o cualquier otro API Request Builder para probar tu API.

|  |  |
| ------ | -------- |
| Method | DELETE |
| URL: | `/todos/<int:position>` |
| Request Body | empty |
