# `03.3` Your first Endpoint (ruta)

Como Flask es un servidor, no tiene sentido no añadirle URLs para exponerlas/publicarlas en internet, por ejemplo:

Como desarrollador, si quisieramos que las personas visitaran http://mydomain.com/hello y les apareciera un mensaje `Hello World`, tendríamos que añadir el siguiente endpoint al archivo `app.py`:

```python
@app.route('/blabla', methods=['GET'])
def hello_world():
    return 'Hello, World!'
```

+ La primera línea `@app.route('/blabla')` especifica el endpoint que estará disponible desde ahora en adelante, en este caso `mydomain.com/blabla`.

+ La primera línea también especifica el método que se usará con esa URL, en este caso es el método `GET` (para obtener info).

+ La segunda línea define una función que será llamada por Flask cuando ese endpoint sea llamado por el usuario (cuando el usuario use `/hello`).

+ La tercera línea retorna el texto: `Hello World` al cliente o navegador que lo solicite.

## 📝Instrucciones:

1. Usando ese conocimiento, haz que tu servidor retorne el string `"<h1>Hello!</h1>"` cuando la URL `/todos` se ingrese en el navegador.

2. Asegúrate que estas líneas siempre sean las dos últimas de tu archivo `app.py`.

```python
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
```
