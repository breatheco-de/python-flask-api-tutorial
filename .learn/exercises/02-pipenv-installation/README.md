# `02` Initialize Pipenv

It is possible to have several python projects with different versions of python, that's why you need to specify which python version you want to use for every project during setup.

In this case, we don't care which version of python we use as long as it's more than 3.0.

Every python project should be wrapped in a "virtual environment" to ensure that each of them have their own Python version, modules and libraries. Make sure nothing gets installed globally in your computer, only install inside the specified environment under the `.venv` folder.

## 📝 Instructions:

1. Run the following command to create a new virtual environment with python 3 on it:

```bash
$ pipenv --three
```

You should see a **PipFile** on the root of your project and it should have inside a **[requires]** for python version 3+ similar to this one (but maybe with a different python 3 version).

![Pipfile preview](../../assets/pipfile.png?raw=true)

Test your step and click `next →` continue.
