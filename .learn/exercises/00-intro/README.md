# Welcome to Flask!

In this tutorial we are going to be building a REST API that exposes 3 endpoints to the internet:

```txt
GET /todos
POST /todos
DELETE /todos/<int:position>
```

## **GET /todos** 

It will return the list of all todos like this:

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

## **POST /todos**

It's going to add a new todo to the list by sending the following request body:

```javascript
{
    "done": true,
    "label": "Sample Todo 3"
}
```

And then, it returns the updated list of todos:

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

## **DELETE /todos/<int:position>**

It's going to remove one todo based on a given position at the end of the url, and return the updated list of todos.
