## `03.3` You first Endpoint (route)

Being Flask a server, it does not make sense not to add any URLs to expose over the internet, for example:

As a developer, if we would like for people to visit http://mydomain.com/hello and get a message "Hello World", we would have to add the following endpoint to the app.py file:

```python
@app.route('/blabla', methods=['GET'])
def hello_world():
    return 'Hello, World!'
```

1. The first line `@app.route('/blabla')` specifies the enpoint that will be available from now on, in this case `mydomain.com/blabla`
2. The first line also specifies the methods that can be used with that URL, in this case `GET` method (for reading).
2. The second line defines a function that will be called by Flask when that endpoint is called by the user (when the user requests `/hello`).
3. The third line returns the text: "Hello World" to the requesting client or browser.


## 📝Instructions

Using that knowledge, make your server return the string `"<h1>Hello!</h1>"` when the URL `/todos` is typed on the browser.
