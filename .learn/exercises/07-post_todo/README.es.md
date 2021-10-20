# `07` POST /todos (añade un nuevo task)

Ahora que ya está hecho el mñetodo GET `/todos`, debemos pensar en el resto de los endpoints de nuestra API:

```txt
GET /todos
POST /todos
DELETE /todos
```

Para poder contruir el `POST /todos` debemos hacer algo similar a lo wue hicimos en el primer endpoint, recuerda que cada endpoint en una Flask API está representada por una función y decorador como este:


```python
@app.route('/blabla', methods=['GET'])
def hello_world():
    return 'Hello, World!'
```

Pero en este caso no esperaremos una solicitud `GET`.

También, esperamos recibir el TODO (tarea) que el cliente quiere añadir dentro del cuerpo de la solicitud (Request Body), solo que en este caso, no esperaremos una solicitud (request) GET.

Esperamos recibir el TODO que el cliente desea añadir dentro del request body.


```python
from flask import request

# # el request body o cuerpo de la solicitud ya fue decodifido por json y se encuentra en la variable request.data  
print(request.data)
```

## 📝 Instrucciones:

1. Añade el siguiente endpoint a tu archivo `app.py` y pruébalo:

```python
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    print("Incoming request with the following body", request_body)
    return 'Response for the POST todo'
```

2. Recuerda añadir el `import request` al comienzao del archivo:


```python
from flask import request
```
