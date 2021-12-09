# Todo List API in Python Flask

<a href="https://www.breatheco.de"><img height="280" align="right" src="https://raw.githubusercontent.com/breatheco-de/python-flask-api-tutorial/3ffb90ea974146f57a3bdfd59665b4c4d5d05197/.breathecode/assets/badge.svg"></a>

Este es un tutorial interactivo que te enseñará cómo crear una API usando el framework Python Flask y Pipenv

## 🌱  Cómo iniciar este proyecto

Este proyecto viene con los archivos necesarios para empezar a trabajar, pero tienes dos opciones para empezar:

a) Abrir este enlace con Gitpod en tu navegador: https://gitpod.io#https://github.com/breatheco-de/python-flask-api-tutorial

b) Clonar este repositorio localmente en tu computador:
```sh
$ git clone https://github.com/breatheco-de/python-flask-api-tutorial
```

💡 Importante: Recuerda actualizar el `remote` del proyecto con el de tu repositorio usando `git remote set-url origin <your new url>`, y luego guardar tu código en tu nuevo repositorio usando `add`, `commit` y `push`.

## Acerca del proyecto que vamos a construir

En este tutorial, crearemos una API REST que expone 3 endpoints a Internet:

```txt
GET /todos
POST /todos
DELETE /todos/<int:position>
```

### GET /todos

Devolverá una lista con to-dos o tareas, asi:
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

Agregará una nueva tarea o to-do a la lista, y recibirá el siguiente request body:

```javascript
{
    "done": true,
    "label": "Sample Todo 1"
}
```

Y devolverá la lista de tareas o to-dos actualizada.

### DELETE /todos/<int:position>

Eliminará una tarea pendiente en función de una posición determinada al final de la URL y devolverá la lista actualizada de tareas pendientes.
