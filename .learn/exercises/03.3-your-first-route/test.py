import toml, pytest, os, sys, tempfile, mock, re
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

@pytest.mark.it("folder /src must exist")
def test_src_folder():
  assert os.path.isdir("./src/")

@pytest.mark.it("app.py must exist")
def test_pipfile_exists():
  assert os.path.isfile("src/app.py")

@pytest.mark.it("Make sure to declare the function hello_world with the @app.route decorator")
def test_add_function():
    from src.app import hello_world
    assert callable(hello_world)

@pytest.mark.it("Make sure to add this decorator above the function hello_world: @app.route('/todos', methods=['GET'])")
def test_declare_variable2():
    path = 'src/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"@app\.route(\s*)\((\s*)'\/[a-zA-Z0-9]+'(\s*),(\s*)methods=(\s*)\[(\s*)'GET'(\s*)\](\s*)\)")
        assert bool(regex.search(content)) == True

@pytest.mark.it("Make sure '/todos' is the route you specified inside the @app.route decorator")
def test_declare_variable3():
    path = 'src/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"'\/todos'")
        assert bool(regex.search(content)) == True

@pytest.mark.it("Endpoint for path '/todos' must exist")
def test_hello_function(client):
    response = client.get('/todos')
    assert isinstance(response.data, str)

@pytest.mark.it("Endpoint for path '/todos' must return <h1>Hello!</h1>")
def test_hello_function(client):
    response = client.get('/todos')
    assert b'<h1>Hello!</h1>' == response.data

    
