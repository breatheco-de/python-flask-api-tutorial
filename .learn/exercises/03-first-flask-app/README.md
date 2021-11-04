## `03` First Flask App

Flask is an app that behaves like a web server: it exposes (publishes) a group of URLs to the internet (like an API or website). 

For example, you can use Flask with a domain and expose the following URLs to the internet: 

```txt
myporfolio.com/home
myporfolio.com/about-me
myporfolio.com/contact-me
```

Those three URLs exposed by Flask will become your personal portfolio website.

To create our first server, we need to add the following two lines to any python file:

```python
from flask import Flask
app = Flask(__name__)
```
## 📝 Instructions:

1. On the root of your project create a `src` folder.  

2. Inside of it, create a file `src/app.py`. 

3. As instructed above, add the code to create a new flask app.
