# `03` First Flask App

Flask is an app that behaves like a web server: it exposes (publishes) a group of URLs to the internet (like an API or website). 

To create our first server, we need to add the following two lines to our Python file that we are going to create (These two lines have to be in every flask project you create to work correctly):

```python
from flask import Flask
app = Flask(__name__)
```

## 📝 Instructions:

1. On the root of your project, create a `src` folder.  

2. Inside of it, create a file named `app.py`. 

3. As instructed above, add the code to create a new Flask app.
