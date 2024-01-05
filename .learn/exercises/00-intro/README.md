# Welcome to Flask!

In this tutorial, we are going to be building a REST API that exposes 3 endpoints to the Internet:

```txt
GET /todos
POST /todos
DELETE /todos/<int:position>
```

## GET /todos

It will return the list of all todos in a JSON format like this:

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

The POST method is going to add a new todo to the list by sending the following request body:

```javascript
{
    "done": true,
    "label": "Sample Todo 3"
}
```

And then it returns the updated list of todos:

```javascript
[
    {
        "done": true,
        "label": "Sample Todo 1"
    },
    {
        "done": true,
        "label": "Sample Todo 2"
    },
    {
        "done": true,
        "label": "Sample Todo 3"
    }
]
```

## DELETE /todos/<int:position>

The DELETE method is going to remove one todo based on a given position at the end of the URL and return the updated list of todos.
