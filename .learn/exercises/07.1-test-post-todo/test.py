import toml
import pytest
import os
import sys
import tempfile
import mock
import json
from flask import Flask


@pytest.fixture
def client():
    with mock.patch('flask.Flask', lambda x: Flask(x)):
        from src.app import app
        db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        app.config['TESTING'] = True

        with app.test_client() as client:
            # with app.app_context():
            #     app.init_db()
            yield client

        os.close(db_fd)
        os.unlink(app.config['DATABASE'])


@pytest.mark.it("Folder src must exist")
def test_src_folder():
    assert os.path.isdir("./src/")


@pytest.mark.it("File app.py must exist")
def test_pipfile_exists():
    assert os.path.isfile("src/app.py")


@pytest.mark.it("Declare a global variable todos, outside any function")
def test_todos_exist():
    from src import app
    try:
        app.todos
    except AttributeError:
        raise AttributeError("The variable 'todos' should exist on app.py")


@pytest.mark.it("Variable todos must be a list")
def test_todos_should_be_list():
    from src import app
    assert isinstance(app.todos, list)


@pytest.mark.it("The global todos list needs to have at least one dummy todo with the required format")
def test_one_dummy():
    from src import app
    assert len(app.todos) > 0


@pytest.mark.it('Each item inside the global todos list should have the following format: { "label": "Sample", "done": True }')
def test_items_format():
    from src import app
    for task in app.todos:
        assert "label" in task
        assert "done" in task


@pytest.mark.it('Each item inside the global todos variable should be a dictionary with two keys: "label" and "done"')
def test_label_and_done():
    from src import app
    for task in app.todos:
        assert "label" in task
        assert "done" in task


@pytest.mark.it('The value of the "label" of each of the todos should be a string')
def test_labels_string():
    from src import app
    for task in app.todos:
        if "label" in task:
            assert isinstance(task["label"], str)


@pytest.mark.it('The value of the "done" key on each todo should be a boolean')
def test_done_bool():
    from src import app
    for task in app.todos:
        if "done" in task:
            assert isinstance(task["done"], bool)


@pytest.mark.it("The response of the hello_world function should be a json, remember to use jsonify")
def test_return(client):
    response = client.get('/todos')
    _body = json.loads(response.data)
    assert isinstance(_body, list)


@pytest.mark.it("Pass the todo list to the jsonify function and return the output of the function")
def test_return_json(client):
    response = client.get('/todos')
    _body = json.loads(response.data)

    for task in _body:
        assert "label" in task
        assert "done" in task


@pytest.mark.it("The function add_new_todo should be declared")
def test_add_new_todo():
    from src import app
    try:
        app.add_new_todo
        assert callable(app.add_new_todo)
    except AttributeError:
        raise AttributeError(
            "The function 'add_new_todo' should exist on app.py")


@pytest.mark.it("The endpoint POST /todos should exist")
def test_return_endpoint(client):
    response = client.post('/todos', json=json.dumps({}))
    assert response.status_code in [200, 201]
