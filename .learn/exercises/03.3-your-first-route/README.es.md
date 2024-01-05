# `03.3` Creating Your First Endpoint (route)

Como Flask es un servidor, no tiene sentido no añadirle URLs para exponerlas/publicarlas en internet, por ejemplo:

Como desarrollador, si quisiéramos que las personas visitaran `http://mydomain.com/myroute` y les apareciera un mensaje `Hello World!`, tendríamos que añadir el siguiente endpoint al archivo `app.py`:

```python
@app.route('/myroute', methods=['GET'])
def hello_world():
    return 'Hello World!'
```

+ La primera línea `@app.route('/myroute')` especifica el endpoint que estará disponible de ahora en adelante, en este caso `mydomain.com/myroute`.

+ La primera línea también especifica el método que se usará con esa URL, en este caso es el método `GET` (para obtener información).

+ La segunda línea define una función que será llamada por Flask cuando ese endpoint sea llamado por el usuario (cuando el usuario use `/myroute`).

+ La tercera línea retorna el texto: `"Hello World!"` al cliente o navegador que lo solicite.

## 📝 Instrucciones:

1. Usando ese conocimiento, haz que tu servidor retorne el string `"<h1>Hello!</h1>"` cuando la URL `/todos` se ingrese en el navegador.

2. Asegúrate que estas líneas siempre sean las dos últimas de tu archivo `app.py`.

```python
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
```
