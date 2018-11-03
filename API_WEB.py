from flask import Flask,jsonify,request,Response
import sys,os.path
from flask.json import JSONEncoder
sys.path.append("src/")
from noticiario import Noticiario

app = Flask(__name__) #creamos la instancia
#embellecedor de JSON desactivado por defecto
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
n = Noticiario()

@app.route("/")
def main():
    return jsonify({
    "status": "OK",
    "ejemplos de Servicios":{
    "CuentaNoticias":{
        "ruta":"/cuentaNoticias",
        "valor": "En mi caso valdría 2"
    },
    "CrearNoticia":
               { "ruta": "/crearNoticia",
                 "valor": "Noticias:<En mi caso valdría 3>"},
    "EditarNoticia":
                {"ruta": "/editarNoticia<&titulo=valor2&descripcion=valor3&categoria=valor4&indice=valor5>",
                "valor": "{Editado: True o False}"
                },
    "EliminarNoticia":{
        "ruta":"/eliminarNoticia<&indice=valor2>",
        "valor": "{El valor es 2}"
    },
    "MostrarNoticiasCategoria":{
        "ruta":"/mostrarNoticiasCategoira<&categoria=valor2>",
        "valor": "{Numero:<en mi ejemplo 1>}"
    }
    }
    })

@app.route("/cuentaNoticias")
def CuentaNoticias():
    return jsonify(n.cuentaNoticias())


@app.route("/crearNoticia")
def CrearNoticia():
    return jsonify(Noticias=n.crear_Noticia())

@app.route("/editarNoticia")
def EditarNoticia():
    if request.args.get('titulo'):
        titulo=(request.args.get('titulo'))
    elif:
        return False
    if request.args.get('descripcion'):
        descripcion=(request.args.get('descripcion'))
    elif:
        return False
    if request.args.get('categoria'):
        categoria=(request.args.get('categoria'))
    elif:
        return False
    if request.args.get('indice'):
        indice=(request.args.get('indice'))
    elif:
        return False
    return jsonify(Editado=n.editarNoticia(titulo,descripcion,categoria,indice))

@app.route("/eliminarNoticia")
def EliminarNoticia():
    if request.args.get('indice'):
        indice=request.args.get('indice')
    elif:
        return False
    return jsonify(n.eliminarNoticia(indice))

@app.route("/mostrarNoticiasCategoira")
def MostrarNoticiasCategoria():
    if request.args.get('categoria'):
        categoria=request.args.get('categoria')
    elif:
        return False
    return jsonify(Numero=n.mostrarNoticiasCategoira(categoria))

@app.errorhandler(404)
def page_not_found(error):
  		return "Página no encontrada", 404

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
