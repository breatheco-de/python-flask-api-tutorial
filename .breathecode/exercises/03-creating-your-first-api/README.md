## `03` Creating your first API Server

Flask is a server that when runned it exposes (publishes) a URL to the internet.

## 📝Instructions

On the root of your project create a `src` folder and inside of it create a file `src/app.py` and add the following content inside of it:

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=False)
```
