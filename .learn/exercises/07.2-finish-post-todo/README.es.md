# `07.2` Finish the POST /todos

Ahora, si queremos terminar el `post` tenemos que hacer dos acciones específicas:

+ Decodificar el request.data para convertirlo a un diccionario de python.

+ Añadir el diccionario a la lista de todos.

+ Retornar la nueva lista de todos.

Para decodificar cualquier string json y convertirlo a un objeto de python podemos usar esta función:

```python
import json
decoded_object = json.loads(original_string)
```

## 📝 Instrucciones:

1. Usa la función json.loads para decodificar el `request.data`

2. Añade el objeto decodificado a la lista de `todos`.

3. Retorna la lista jsonify de los `todos` actualizados.
