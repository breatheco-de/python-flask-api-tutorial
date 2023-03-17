# `07.2` Finish the POST /todos

Ahora... si queremos terminar el post, tenemos que realizar estas acciones específicas:

+ Primero asegúrate de convertir el cuerpo de la solicitud en una estructura de datos real de Python, como un diccionario. Ya usamos `request.json` para eso, ya que sabemos que la solicitud estará en formato application/json. Si eso no se conoce, es posible que desee usar `request.get_json(force=True)` para ignorar el tipo de contenido y tratarlo como json.

+ Agrega el diccionario a la lista de `todos`.

+ Devuelve la nueva lista de `todos`.

Tu código debería verse así ahora:

```python

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    return 'Response for the POST todo'

```

Obviamente, este punto final actualmente no agrega nada nuevo a nuestra 'base de datos' (la lista `todo`).

Completemos el código para que el punto final pueda hacer tu trabajo: agregar una nueva tarea a los `todos`.

## 📝 Instrucciones:

1. Agrega el contenido del cuerpo de la solicitud decodificada a la lista `todos`.

2. Devuelve la lista actualizada `todos` al front end.

3. No olvide `jsonify` su devolución. ¿Por qué es esto necesario? Discuta con la clase.
