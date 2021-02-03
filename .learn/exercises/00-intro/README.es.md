# Bienvenido a Flask!

En este tutorial vamos a construir una REST API que expone 3 endpoints
internet:

```txt
GET /todos
POST /todos
DELETE /todos/<int:position>
```

### GET /todos

Retornaremos toda la lista de todos así:

```javascript
[
    {
        "done": true,
        "label": "Sample Todo 1"
    },
    {
        "done": true,
        "label": "Sample Todo 2"
    }
]
```

### POST /todos 

Añadirá un nuevo todo a la lista. Recibirá el siguiente request body:

```javascript
{
    "done": true,
    "label": "Sample Todo 1"
}
```

Y retornará la lista actualizada de los todos:

### DELETE /todos/<int:position>

Eliminará un todo basándose en la posición dada al final de la url, y retorna la lista actualizada de todos.

