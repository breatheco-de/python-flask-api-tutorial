# `02` Initialize Pipenv

It is possible to have several Python projects with different versions of Python, that's why you need to specify which Python version you want to use for every project during setup.

In this case, we don't care which version of Python we use as long as it's more than `3.0`.

Every Python project should be wrapped in a "virtual environment" to ensure that each of them have their own Python version, modules and libraries. Make sure nothing gets installed globally in your computer, only install inside the specified environment under the `.venv` folder.

## 📝 Instructions:

1. Run the following command to create a new virtual environment with Python 3 on it:

```bash
$ pipenv install --python 3
```

You should see a **PipFile** on the root of your project and it should have a **[requires]** inside of it for Python version 3+: similar to this one (but maybe with a different Python 3 version).

![Pipfile preview](../../assets/pipfile.png?raw=true)

Follow the steps and click `next →` to continue.
