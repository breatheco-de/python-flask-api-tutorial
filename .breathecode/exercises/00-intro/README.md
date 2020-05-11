# Welcome to Flask!

In this tutorial we are going to be building a REST API that exposes 4 endpoints to the internet:

```txt
GET /todos
POST /todos
DELETE /todos
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

### DELETE /todos/<position:int>

It's going to remove one todo based on a given position at the end of the url, and return the updated list of todos.
