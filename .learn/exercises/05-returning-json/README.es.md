# `05` Returning JSON

Las REST APIs tienen que retornar datos en formato JSON, no en formato HTML.

Puedes usar la función [flask jsonify](https://flask.palletsprojects.com/en/1.1.x/api/#flask.json.jsonify) para convertir con facilidad cualquier tipo de datos básico a JSON de esta forma:

```python
def hello_world():
    # supongamos que tienes some_data (cierta información) en una variable json
    some_data = { "name": "Bobby", "lastname": "Rixer" }

    # puedes convertir esa variable en un string json así
    json_text = flask.jsonify(some_data)

    # y luego puedes retornarla (return) en el response body así:
    return json_text
```

Si aplicamos estos conocimientos a nuestro proyecto de todo-list, podemos crear una variable global  `todos` que va a contener la lista de todos de esta forma:

```python
todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]
```

## 📝 Instrucciones

1. Crea una variable global todos, declárala globalmente. No la declares dentro de una función, declárala en cualquier lado pero a nivel global. Asegúrate de que la variable contenga por lo menos una tarea (task) con la siguiente estructura:

```python
{ "label": "My first task", "done": False }
```

2. Cambia la declaración del return de tu método `hello_world` para que retorne la versión jsonify de los todos globales.
