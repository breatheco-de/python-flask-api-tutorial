## `03.1` You first route

Being Flask a server, it does not make sense to create a flask app without adding any URLs to expose over the internet, for example:

As a developer, if we would like for people to visit http://mydomain.com/hello and get a message "Hello World", we would have to add the following route to the app.py file:

```python
@app.route('/hello')
def hello_world():
    return 'Hello, World!'
```

1. The first line `@app.route('/')` specifies the end of the URL (the path).
2. The second line creates a function that will be called by Flask when that path is called by the user.
3. The third line returns the "Hello World" to the requesting client or browser.


## 📝Instructions

Make your server return the string `"<h1>Hello!</h1>"` when the URL `/hello` is tiped on the browser.

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=False)
```
