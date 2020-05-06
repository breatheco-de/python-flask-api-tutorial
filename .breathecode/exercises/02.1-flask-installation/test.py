import toml, pytest, os

@pytest.mark.it("Pipfile must exist")
def test_pipfile_exists():
  assert os.path.isfile("Pipfile")

@pytest.mark.it("Python version on Pipfile must be 3+")
def test_pipfile_contains_python_version():
  with open("Pipfile", "r") as f:
    toml_content = f.read()
    parsed_toml = toml.loads(toml_content)
    assert parsed_toml["requires"]["python_version"][0:2] == "3."

@pytest.mark.it("Flask must exist on the pipfile dependency [packages]")
def test_pipfile_contains_flask():
  with open("Pipfile", "r") as f:
    toml_content = f.read()
    parsed_toml = toml.loads(toml_content)
    keys = parsed_toml["packages"].keys()
    assert "flask" in keys
