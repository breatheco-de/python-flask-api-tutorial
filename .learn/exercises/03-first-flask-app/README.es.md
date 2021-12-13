# `03` First Flask App

Flask es una app que se comporta como un servidor web, es decir que expone (publica) un grupo de URLs en internet (como una api o un sitio web).

Por ejemplo, puedes usar Flask con un dominio y exponer las siguientes URLs en internet:

```txt
myporfolio.com/home
myporfolio.com/about-me
myporfolio.com/contact-me
```

Esas 3 URLs expuestas por Flask se convertirán en tu postafolio personal de sitios webs.

Para crear nuestro primer servidor debemos añadir las siguientes dos líneas en cualquier archivo de Python:


```python
from flask import Flask
app = Flask(__name__)
```
## 📝 Instrucciones:

1. En la raíz del proyecto crea una carpeta llamada `src`.

2. Dentro de ella, crea un archivo `src/app.py`. 

3. Añade el código necesario para crear una nueva app Flask especificada en las intrucciones anteriores.

 
