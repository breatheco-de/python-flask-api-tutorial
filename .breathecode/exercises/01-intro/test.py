import sys, pytest, subprocess


@pytest.mark.it("You need to have python3 installed")
def test_python3_exists():
  assert sys.version_info.major == 3

@pytest.mark.it("You need to have pipenv installed")
def test_pipenv_exists():
  code = subprocess.call(['which', 'pipenv'])
  assert code == 0

