# `07.1` Test your endpoint

Hasta ahora esto lo que tienes sobre el endpoint `POST /todos`, tomate el tiempo para analizar cada línea:

```python
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    print("Incoming request with the following body", request_body)
    return 'Response for the POST todo'
```

Usa postman, insomnia o cualquier otro API Request Builder que quieras para probar tu API.

|  |  |
| ------ | -------- |
| Method | Post |
| URL: | /todos |
| Request Body | `{ "done": true, "label": "Sample Todo 1" }` |
