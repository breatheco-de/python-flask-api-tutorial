## `07` POST /todos (añade un nuevo task)

Ahora que ya está hecho el mñetodo GET `/todos`, debemos pensar en el resto de los endpoints de nuestra API:

```txt
GET /todos
POST /todos
DELETE /todos
```
Para poder contruir el `POST /todos` debemos hacer algo similar a lo wue hicimod en el primer endpoint
In order to build the `POST /todos`, recuerda que cada endpoint en una Flask API está representada por una función y decorador como este:


```python
@app.route('/blabla', methods=['GET'])
def hello_world():
    return 'Hello, World!'
```

Pero en este caso no esperaremos una solicitud `GET`.

También, esperamos recibir el TODO (tarea) que el cliente quiere añadir dentro del cuerpo de la solicitud (Request Body).
