import toml, pytest, os, sys, tempfile, mock
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

@pytest.mark.it("folder src must exist")
def test_src_folder():
  assert os.path.isdir("./src/")

@pytest.mark.it("app.py must exist")
def test_pipfile_exists():
  assert os.path.isfile("src/app.py")

@pytest.mark.it("Python file content must be exaclty as specified")
def test_import_hello():
  with open("src/app.py", "r") as f:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    f_model = open(dir_path+"/example_app.py", "r")
    model = f_model.read()
    f_model.close()

    content = f.read()
    result = content.find(model)
    print("result", content)
    assert result > -1

@pytest.mark.it("Endpoint for path '/' must exist and return hello world")
def test_empty_db(client):
    response = client.get('/')
    assert b'Hello, World!' == response.data
