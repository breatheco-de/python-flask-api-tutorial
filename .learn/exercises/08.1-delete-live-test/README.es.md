## `08.1` Prueba tu endpoint

Hasta ahora esto es lo que tienes sobre el endpoint  `DELETE /todos/<int:position>`, tomate tu tiempo para analizar cada línea:

```python
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    return 'something'
```

Usa postman, insomnia o cualquier otro API Request Builder para probar tu API, aquí hay un ejemplo de como hacerlo con postwoman:
https://youtu.be/HEQ-pSgOVtY

|  |  |
| ------ | -------- |
| Method | DELETE |
| URL: | `/todos/<int:position>` |
| Request Body | empty |