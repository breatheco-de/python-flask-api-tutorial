import toml, pytest, os, sys, tempfile, mock, http.client, socket

def isOpen(ip,port):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      s.connect((ip, int(port)))
      s.shutdown(2)
      return True
   except:
      return False

@pytest.mark.it("Make sure your app server is running, did you run the app.py?")
def test_import_hello():
  assert isOpen('0.0.0.0', 3245)
