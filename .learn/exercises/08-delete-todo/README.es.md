# `08` Delete todo

Eliminar un todo es básicamente lo opuesto a añadir un nuevo todo, pero el código de la feature `POST /todos` es 90% reutilizable.

La principal diferencia es que `DELETE /todos/<position:int>` recibirá la posición para eliminar en la URL de la solicitud.

```python
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    return 'something'
```

Cuando usas los símbolos `<` y `>`, Flask retornará lo que sea que haya especificado el cliente en esa parte de la URL como variable. por ejemplo:

```txt
La solicitud DELETE /todos/1 llamará a la función `delete_todo` con la variable position == 1
La solicitud DELETE /todos/323 llamará a la función `delete_todo` con la variable position == 323
```
## 📝 Instrucciones:

1. Añade este endpoint a tu archivo `app.py`.
