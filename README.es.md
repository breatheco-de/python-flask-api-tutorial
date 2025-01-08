<!--hide-->
# API de Lista de Tareas en Python Flask
<!--endhide-->

Este es un tutorial interactivo que te enseñará cómo crear una API usando el framework Python Flask y Pipenv

<onlyfor saas="false" withBanner="false">
    
## 🌱 Cómo comenzar este proyecto

Hay dos formas de empezar:

a) Abrir este enlace con [Codespaces](https://4geeks.com/es/lesson/tutorial-de-github-codespaces) (recomendado) o [Gitpod](https://4geeks.com/es/lesson/como-utilizar-gitpod) en tu navegador: https://github.com/codespaces/new/?repo=4GeeksAcademy/python-hello

b) Clonar este repositorio localmente en tu computador:

```sh
$ git clone https://github.com/4GeeksAcademy/python-hello
```

### Pasos

- Si trabajas localmente, debe tener python [instalado](https://4geeks.com/es/how-to/como-instalar-python).

- Deberías abrir el terminal en la ruta de esta plantilla y ejecutar `$ python3 app.py`, si todo funciona correctamente, debería mostrar `Hello World` en el terminal.

- Puedes probar tu código escribiendo `$ python3 test.py`.

💡 Importante: Recuerda actualizar el `remote` del proyecto con el de tu repositorio usando `git remote set-url origin <your new url>`, y luego guardar tu código en tu nuevo repositorio usando `add`, `commit` y `push`.

</onlyfor>

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
