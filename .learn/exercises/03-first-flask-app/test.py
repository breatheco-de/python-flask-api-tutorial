import toml, pytest, os, sys, tempfile, mock, re
import flask
@pytest.mark.it("Folder src must exist")
def test_src_folder():
  assert os.path.isdir("./src/")

@pytest.mark.it("File src/app.py must exist")
def test_pipfile_exists():
  assert os.path.isfile("src/app.py")

@pytest.mark.it("Import flask correctly")
def test_declare_variable():
    with open("src/app.py", 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"from(\s*)flask(\s*)import(\s*)Flask")
        assert bool(regex.search(content)) == True

@pytest.mark.it("Create variable app with a Flask object assined")
def test_declare_variable():
    from src.app import app
    assert isinstance(app, flask.Flask)
