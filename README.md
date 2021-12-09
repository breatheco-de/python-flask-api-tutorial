# Todo List API in Python Flask

<a href="https://www.breatheco.de"><img height="280" align="right" src="https://raw.githubusercontent.com/breatheco-de/python-flask-api-tutorial/3ffb90ea974146f57a3bdfd59665b4c4d5d05197/.breathecode/assets/badge.svg"></a>

This is an interactive tutorial that will teach you how to create an API using the Python Flask framework using Python and Pipenv.

## 🌱  How to start this project

This project comes with the necessary files to start working, but you have two options to start:

a) Open this link in your browser to clone it with gitpod: https://gitpod.io#https://github.com/breatheco-de/python-flask-api-tutorial

b) You can clone this repository on your local computer:
```sh
$ git clone https://github.com/breatheco-de/python-flask-api-tutorial
```
💡 Important: Remember to create a new repository, update the remote (`git remote set-url origin <your new url>`), and upload the code to your new repository using `add`, `commit` and `push`.


## About the project we are going to build

In this tutorial we are going to be building a REST API that exposes 3 endpoints to the internet:

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

It's going to add a new todo to the list, it will receive the following request body:

```javascript
{
    "done": true,
    "label": "Sample Todo 1"
}
```

And return the updated list of todos.

### DELETE /todos/<int:position>

It's going to remove one todo based on a given position at the end of the url, and return the updated list of todos.

