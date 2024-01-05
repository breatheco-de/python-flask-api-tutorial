# `03.1` Running your new application

After creating our app, we need to run and start the application.

When the application runs, it will take over your command line, and you will not be able to type on it anymore because a server application (like Flask) never stops running. It keeps waiting for "requests" forever.

## 📝 Instructions:

1. Add the following lines at the bottom of your `app.py` file (Remember, this should be inside of your `src` folder on the root directory):

```python
# These two lines should always be at the end of your app.py file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
```

> These two lines should always be at the very end of your file.

To run your new server, open a **new separate terminal** and enter the following command:

```bash
$ pipenv run python src/app.py
```

> Open a new terminal to run this command.

![Running Terminal](../../assets/running-flask-app.gif?raw=true)

The way this command works is we use our combined `pipenv` command to start up our virtual environment and *run* it using Python. Our target file for starting our server for future requests is `src/app.py`.
