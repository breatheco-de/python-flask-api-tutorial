# `05` Returning JSON

Las REST APIs tienen que retornar datos en formato JSON, no en formato HTML.

Puedes usar la función [flask jsonify](https://flask.palletsprojects.com/en/3.0.x/api/#flask.json.jsonify) para convertir con facilidad cualquier tipo de datos básico a JSON de esta forma:

```python
# Añade el método jsonify a tu importación de Flask
from flask import Flask, jsonify

# Supongamos que tienes tus datos en la variable some_data
some_data = { "name": "Bobby", "lastname": "Rixer" }

@app.route('/myroute', methods=['GET'])
def hello_world():
    # Puedes convertir esa variable en una cadena json de la siguiente manera
    json_text = jsonify(some_data)

    # Y luego puedes devolverlo al front-end en el cuerpo de la respuesta de la siguiente manera
    return json_text
```

Si aplicamos estos conocimientos a nuestro proyecto de todo-list, podemos crear una variable global `todos` que va a contener la lista de todos de esta forma:

```python
todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]
```

## 📝 Instrucciones:

1. Crea una variable global `todos`, declárala globalmente. No la declares dentro de una función, declárala en cualquier lado pero a nivel global. Asegúrate de que la variable contenga por lo menos una tarea (task) con la siguiente estructura:

```python
[ { "label": "My first task", "done": False } ]
```

2. Cambia la función del endpoint de tu método GET para que retorne la versión en json (Usando jsonify) de la variable de `todos` recién creada.
