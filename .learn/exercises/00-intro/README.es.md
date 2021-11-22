# Bienvenido a Flask!

En este tutorial vamos a construir una REST API que expone 3 endpoints
internet:

```txt
GET /todos
POST /todos
DELETE /todos/<int:position>
```

## GET /todos

Retornaremos toda la lista de to-dos así:

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

## POST /todos 

Añadirá un nuevo to-do a la lista. Recibirá el siguiente request body:

```javascript
{
    "done": true,
    "label": "Sample Todo 1"
}
```

Y retornará la lista actualizada de los to-dos:

## DELETE /todos/<int:position>

Eliminará un to-do basándose en la posición dada al final de la url, y retorna la lista actualizada de to-dos.

