<!--hide-->
# Todo List API in Python Flask

<a href="https://www.breatheco.de"><img height="280" align="right" src="https://raw.githubusercontent.com/breatheco-de/python-flask-api-tutorial/3ffb90ea974146f57a3bdfd59665b4c4d5d05197/.breathecode/assets/badge.svg"></a>
<!--endhide-->

Este es un tutorial interactivo que te enseñará cómo crear una API usando el framework Python Flask y Pipenv

## 🌱 Cómo comenzar este proyecto

Este proyecto viene con los archivos necesarios para comenzar a trabajar de inmediato.

Recomendamos abrir este mismo repositorio usando un entorno de desarrollo como [Codespaces](https://4geeks.com/es/lesson/tutorial-de-github-codespaces) (recomendado) o [Gitpod](https://4geeks.com/es/lesson/como-utilizar-gitpod). Alternativamente, puedes clonarlo en tu computadora local usando el comando `git clone`.

Este es el repositorio que necesitas abrir:

```text
https://github.com/breatheco-de/python-flask-api-tutorial
```

**👉 Por favor sigue estos pasos sobre** [cómo comenzar un proyecto de programación](https://4geeks.com/es/lesson/como-comenzar-un-proyecto-de-codificacion).

> 💡 Importante: Recuerda guardar y subir tu código en GitHub creando un nuevo repositorio, actualizando el remoto (`git remote set-url origin <your new url>`) y subiendo el código a tu nuevo repositorio usando los comandos `add`, `commit` y `push` desde la terminal de git.

## Acerca del proyecto que vamos a construir

En este tutorial, crearemos una API REST que expone 3 endpoints a Internet:

```txt
GET /todos
POST /todos
DELETE /todos/<int:position>
```

### GET /todos

Devolverá una lista con to-dos o tareas, así:

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

Eliminará una tarea en función de una posición determinada al final de la URL y devolverá la lista actualizada de tareas pendientes.

Este y otros proyectos son usados para [aprender a programar](https://4geeksacademy.com/es/aprender-a-programar/aprender-a-programar-desde-cero) por parte de los alumnos de 4Geeks Academy [Coding Bootcamp](https://4geeksacademy.com/us/coding-bootcamp) realizado por [Alejandro Sánchez](https://twitter.com/alesanchezr) y muchos otros contribuyentes. Conoce más sobre nuestros [Cursos de Programación](https://4geeksacademy.com/es/curso-de-programacion-desde-cero?lang=es) para convertirte en [Full Stack Developer](https://4geeksacademy.com/es/coding-bootcamps/desarrollador-full-stack/?lang=es), o nuestro [Data Science Bootcamp](https://4geeksacademy.com/es/coding-bootcamps/curso-datascience-machine-learning).
