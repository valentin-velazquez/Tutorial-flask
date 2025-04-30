from flask import Flask, url_for
import sqlite3

app = Flask(__name__)

@app.route("/")
def hello_world():
    
    url_hamburguesa = url_for("COMIDA_condimentos", condimentos="cheddar")
    url_papas = url_for("acompañamiento")
    url_dados = url_for("dado", caras=6)
    url_sumar = url_for("suma", n1=4, n2=9)
    url_logo  =  url_for("static", filename="logo.png")
    url_insertar = url_for("insertar", nombre = "valen", email = "valesergiovelazquez@gmail.com")
    url_borrar = url_for("borrar", id = "2")
    url_mostrar = url_for("mostrar", id = "1")

    
    
    return f"""
    <ul>
       <li><a href='{url_hamburguesa}'>HAMBUERGUESA</a></li>
       <li><a href='{url_papas}'>papas_fritas</a></li>
       <li><a href='{url_dados}'>dados</a></li>
       <li><a href='{url_sumar}'>sumar</a></li>
       <li><a href='{url_logo}'>logo</a></li>
       <li><a href='{url_insertar}'>insertar</a></li>
       <li><a href='{url_borrar}'>borrar</a></li>
       <li><a href='{url_mostrar}'>mostrar</a></li>
       <ul>

"""
    

@app.route("/HAMBUERGUESA")
def COMIDA():
    return "<h2>amo las hamburguesas</h2>"

@app.route("/HAMBUERGUESA/<string:condimentos>")
def COMIDA_condimentos(condimentos):
    return f"<h2>amo las hamburgeesas {condimentos}</h2>"

@app.route("/papas_fritas")
def acompañamiento():
    return "<h2>amo las papas fritas</h2>"

@app.route("/dado/<int:caras>")
def dado(caras):
    from random import randint
    numero = randint(1,caras)
    return f"<h2>dado de {caras} caras, salio {numero}!</h2>"

@app.route("/sumar/<int:n1>/<int:n2>")
def suma(n1,n2):
    suma = n1+n2
    return f"<h2>{n1} mas {n2} da {suma}</h2>"


db=None
def abrirConexion():
    db = sqlite3.connect("instance/datos.sqlite")
    db.row_factory = sqlite3.Row
    return db


def cerrarConexion():
    global db
    if db is not None:
        db.close()
        db=None

@app.route("/usuarios")
def obterGente():
    global db 
    conexion = abrirConexion()
    cursor = conexion.cursor ()
    cursor.execute('SELECT * FROM usuarios')
    resultado = cursor.fetchall()#te trae a toda la tabla el fetchall
    fila = [dict(row) for row in resultado]

    return fila             














db = None


def dict_factory(cursor, row):
  """Arma un diccionario con los valores de la fila."""
  fields = [column[0] for column in cursor.description]
  return {key: value for key, value in zip(fields, row)}


def abrirConexion():
   global db
   db = sqlite3.connect("instance/datos.sqlite")
   db.row_factory = dict_factory


def cerrarConexion():
   global db
   db.close()
   db = None


@app.route("/test-db")
def testDB():
   abrirConexion()
   cursor = db.cursor()
   cursor.execute("SELECT COUNT(*) AS cant FROM usuarios; ")
   res = cursor.fetchone()
   registros = res["cant"]
   cerrarConexion()
   return f"Hay {registros} registros en la tabla usuarios"



@app.route("/insertar/<string:nombre>/<string:email>")
def insertar(nombre, email):
    abrirConexion()
    db.execute("INSERT INTO usuarios(usuario, email) VALUES (?, ?);",(nombre, email))
    db.commit()
    cerrarConexion()
    return f"se agregue el {nombre} y el email{email}"

@app.route("/borrar/<string:id>")
def borrar(id):
    abrirConexion()
    db.execute("DELETE FROM usuarios WHERE id = (?)",(id))
    db.commit()
    cerrarConexion()
    return f"borraste el usuario con el id {id}"



@app.route("/mostrar/<string:id>")
def mostrar(id):
   abrirConexion()
   cursor = db.cursor()
   cursor.execute("SELECT * FROM usuarios WHERE id = ?",(id))
   usuario = cursor.fetchall()
   cerrarConexion()
   
   if usuario:
       return f"{usuario}"
   else:
       return f"no se encontro un usuario con id {id}"


@app.route("/update/<string:id>")
def update(id):
    abrirConexion()
    db.execute("DELETE FROM usuarios WHERE id = (?)",(id))
    db.commit()
    cerrarConexion()
    return f"borraste el usuario con el id {id}"


