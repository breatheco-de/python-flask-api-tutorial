# `03.3` You first Endpoint (route)

Being Flask a server, it does not make sense not to add any URLs to expose over the internet, for example:

As a developer, if we would like for people to visit http://mydomain.com/hello and get a message `Hello World`, we would have to add the following endpoint to the app.py file:

```python
@app.route('/blabla', methods=['GET'])
def hello_world():
    return 'Hello, World!'
```

+ The first line `@app.route('/blabla')` specifies the enpoint that will be available from now on, in this case `mydomain.com/blabla`.

+ The first line also specifies the methods that will be used with that URL, in this case `GET` method (for reading).

+ The second line defines a function that will be called by Flask when that endpoint is called by the user (when the user requests `/hello`).

+ The third line returns the text: "Hello World" to the requesting client or browser.

## 📝Instructions:

1. Using that knowledge, make your server return the string `"<h1>Hello!</h1>"` when the URL `/todos` is typed on the browser.

2. Please make sure that this lines keep being the last two lines of your `app.py` file.

```python
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
```
