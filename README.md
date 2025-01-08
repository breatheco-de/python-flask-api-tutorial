<!--hide-->
# Todo List API in Python Flask
<!--endhide-->

This is an interactive tutorial that will teach you how to create an API using the Flask framework on Python and Pipenv.

<onlyfor saas="false" withBanner="false">
    
## 🌱 How to start this project

There are 2 ways to start:

a) Open this link in your browser with [Codespaces](https://4geeks.com/lesson/what-is-github-codespaces) (recommended) or [Gitpod](https://4geeks.com/lesson/how-to-use-gitpod): https://github.com/codespaces/new/?repo=4GeeksAcademy/python-hello

b) You can clone this repository on your local computer:

```bash
$ git clone https://github.com/4GeeksAcademy/python-hello
```

### Steps

- If working locally, you should have python [installed](https://4geeks.com/how-to/how-to-install-python).

- You should open the terminal on the path of this template and run `$ python3 app.py`, if everything works correctly, it should show `Hello World` on the terminal.

- You can test your code by typing: `$ python3 test.py`.

💡 Important: Remember to create a new repository, update the remote (`git remote set-url origin <your new url>`), and upload the code to your new repository using `add`, `commit` and `push`.

</onlyfor>

## About the project we are going to build

In this tutorial, we are going to be building a REST API that exposes 3 endpoints to the internet:

```txt
GET /todos
POST /todos
DELETE /todos/<int:position>
```

### GET /todos

Will return the list of all todos like this:

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

This will add a new todo to the list with the following request body:

```javascript
{
    "done": true,
    "label": "Sample Todo 1"
}
```

And return the updated list of todos.

### DELETE /todos/<int:position>

This will remove one todo, based on a given position in the todos list, at the end of the URL and return the updated list of todos.

This and many other projects are built by students as part of the 4Geeks Academy [Coding Bootcamp](https://4geeksacademy.com/us/coding-bootcamp) by [Alejandro Sanchez](https://twitter.com/alesanchezr) and many other contributors. Find out more about our [Full Stack Developer Course](https://4geeksacademy.com/us/coding-bootcamps/part-time-full-stack-developer), and [Data Science Bootcamp](https://4geeksacademy.com/us/coding-bootcamps/datascience-machine-learning).

