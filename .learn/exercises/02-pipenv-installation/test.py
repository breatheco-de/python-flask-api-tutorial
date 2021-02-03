import toml, pytest, os

@pytest.mark.it("Pipfile must exist, make sure you initialized the environment")
def test_pipfile_exists():
  assert os.path.isfile("Pipfile")

@pytest.mark.it("Python version on Pipfile must be 3+, did you run $ pipenv --three ?")
def test_pipfile_contains_python_version():
  with open("Pipfile", "r") as f:
    toml_content = f.read()
    parsed_toml = toml.loads(toml_content)
    assert parsed_toml["requires"]["python_version"][0:2] == "3."
