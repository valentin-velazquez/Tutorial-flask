# Tutorial-flask

Para crear un entorno virtual, desde la carpeta del proyecto usar el comando:
python -m venv .venv
Para activar el entorno virtual, desde la carpeta del proyecto usar el comando:
source .venv/bin/activate
Para instalar el flask (en el entorno virtual, después de activarlo) usar el comando:
pip install flask
Para verificar si está instalado el flask usar el comando:
flask --version

Debería figurar la versión 2.3.2 o más nueva.

Para inicializar la base de datos:
flask --app flaskr init-db

Para poner a correr el servidor:
flask --app flaskr run --debug
Para poner a correr el servidor para que además se pueda acceder desde otras computadoras de la red:
flask --app flaskr -h 0.0.0.0 run --debug
