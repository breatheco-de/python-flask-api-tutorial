# `07` POST /todos (add a new task)

Ahora que ya está hecho el método GET `/todos`, debemos pensar en el resto de los endpoints de nuestra API:

```txt
GET /todos
POST /todos
DELETE /todos
```

Para poder construir el `POST /todos` debemos hacer algo similar a lo que hicimos en el primer endpoint, recuerda que cada endpoint en una Flask API está representada por una función y un decorador de esta manera:

```python
@app.route('/myroute', methods=['GET'])
def hello_world():
    return 'Hello World!'
```

Pero en este caso no esperaremos una solicitud `GET`, sino una solicitud `POST`.

También, esperamos recibir el TODO que el cliente quiere añadir dentro del `request_body` (cuerpo de la solicitud).

```python
from flask import request

# El request_body o cuerpo de la solicitud ya está decodificado en formato JSON y se encuentra en la variable request.json  
print(request.json)
```

## 📝 Instrucciones:

1. Añade el siguiente endpoint a tu archivo `app.py` y pruébalo:

```python
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    return 'Response for the POST todo'
```

2. Recuerda añadir el `import request` al comienzo del archivo:

```python
from flask import request
```
