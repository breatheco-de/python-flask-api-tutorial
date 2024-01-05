import toml, pytest, os

@pytest.mark.it("Pipfile must exist")
def test_pipfile_exists():
  assert os.path.isfile("Pipfile")

@pytest.mark.it("Flask must exist on the Pipfile dependency [packages]")
def test_pipfile_contains_flask():
  with open("Pipfile", "r") as f:
    toml_content = f.read()
    parsed_toml = toml.loads(toml_content)
    keys = parsed_toml["packages"].keys()
    assert "flask" in keys
