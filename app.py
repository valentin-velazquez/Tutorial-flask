from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """
           <a href= 'boca'>boca</a>
           <a href= 'riBer'>riBer</a>
    """
    

@app.route("/boca")
def boquita():
    return "<h1>boca el mas grande!</h1>"

@app.route("/riBer")
def riBer():
    return "<h1>riBer equipo chico</h1>"
