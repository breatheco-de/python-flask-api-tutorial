## `03` First Flask App

Flask is a app that behaves like a web server, that means that it exposes (publishes) a group of URLs to the internet (Like and API or website). 

For example, you can use Flask to by a domain and expose the following URLs to the internet: 

```txt
myporfolio.com/home
myporfolio.com/about-me
myporfolio.com/contact-me
```

Those three URL's exposed by Flask will be become your personal portfolio website.

To create our first server we need to add the following two lines to any python file:

```python
from flask import Flask
app = Flask(__name__)
```

## 📝Instructions

1. On the root of your project create a `src` folder.  
2. Inside of it create a file `src/app.py` and add the code to create a new flask app that was specified above the instructions.
