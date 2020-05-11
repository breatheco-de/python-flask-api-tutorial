# Todo List API in Python Flask

<a href="https://www.breatheco.de"><img height="280" align="right" src="https://raw.githubusercontent.com/breatheco-de/python-flask-api-tutorial/3ffb90ea974146f57a3bdfd59665b4c4d5d05197/.breathecode/assets/badge.svg"></a>

This is an interactive tutorial that will teach you how to create an API using the Python Flask framework using Python and Pipenv. Please click here to start the tutorial:

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/breatheco-de/python-flask-api-tutorial)


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

And return the updated list of todos

### DELETE /todos/<int:position>

It's going to remove one todo based on a given position at the end of the url, and return the updated list of todos.

