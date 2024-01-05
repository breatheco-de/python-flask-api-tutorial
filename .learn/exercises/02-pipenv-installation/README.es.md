# `02` Initialize Pipenv

Es posible tener varios proyectos con Python con diferentes versiones de Python, por esta razón debes especificar que versión de Python quieres usar en cada proyecto durante su configuración.

En este caso, no importa que versión de Python usemos mientras sea mayor a la `3.0`.

Cada proyecto de Python debe estar envuelto en un "ambiente virtual" para asegurarse de que cada uno de ellos tenga su propia versión de Python, módulos y librerías, nada se instala globalmente en tu computador, solo se instala dentro del entorno en el que se encuentra en la carpeta `.venv`.

## 📝 Instrucciones:

1. Ejecuta el siguiente comando para crear un nuevo entorno virtual con Python 3:

```bash
$ pipenv install --python 3
```

Deberías ver un **PipFile** en la raíz de tu proyecto y dentro debería tener **[requires]** en la versión de Python 3+ similar a este (pero quizás con una diferente versión de Python 3).

![Pipfile preview](../../assets/pipfile.png?raw=true)

Sigue los pasos y haz clic en `next →` para continuar.
