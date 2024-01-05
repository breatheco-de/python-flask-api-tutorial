<!--hide-->
# Todo List API in Python Flask
<a href="https://www.breatheco.de"><img height="280" align="right" src="https://raw.githubusercontent.com/breatheco-de/python-flask-api-tutorial/3ffb90ea974146f57a3bdfd59665b4c4d5d05197/.breathecode/assets/badge.svg"></a>
<!--endhide-->

This is an interactive tutorial that will teach you how to create an API using the Flask framework on Python and Pipenv.

## 🌱 How to start this project

This project comes with the necessary files to start working immediately.

We recommend opening this very same repository using a provisioning tool like [Codespaces](https://4geeks.com/lesson/what-is-github-codespaces) (recommended) or [Gitpod](https://4geeks.com/lesson/how-to-use-gitpod). Alternatively, you can clone it on your local computer using the `git clone` command.

This is the repository you need to open:

```text
https://github.com/breatheco-de/python-flask-api-tutorial
```

**👉 Please follow these steps on** [how to start a coding project](https://4geeks.com/lesson/how-to-start-a-project).

> 💡 Important: Remember to save and upload your code to GitHub by creating a new repository, updating the remote (`git remote set-url origin <your new url>`), and uploading the code to your new repository using the `add`, `commit` and `push` commands from the git terminal.

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

