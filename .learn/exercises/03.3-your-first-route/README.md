# `03.3` Creating Your First Endpoint (route)

Since Flask is a server, it only makes sense to add some URLs to expose over the internet, for example: `mydomain.com/hello`

As a developer, if we would like people to visit `http://mydomain.com/myroute` and show a message like `Hello World!` to those people, we have to add the following endpoint inside our `app.py` file:

```python
@app.route('/myroute', methods=['GET'])
def hello_world():
    return 'Hello World!'
```

+ The first part, `@app.route('/myroute')`, specifies the endpoint that will be available to our users. In this case, users would see `mydomain.com/myroute` when visiting this route.

+ The first line also specifies the methods that will be used with that URL. In this case, the `GET` method (for reading data).

+ The second line defines a function that will be called by Flask when that endpoint is called by the user (when the user requests `/myroute`).

+ The third line defines our function execution and in this case, returns the text `"Hello World!"` to the requesting client or browser.

## 📝 Instructions:

1. Using that knowledge, make your server return the string `"<h1>Hello!</h1>"` when the URL `/todos` is typed on the browser.

2. Please make sure that these two lines stay at the bottom of your `app.py` file. All routing and functions must remain above these two lines.

```python
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
```
