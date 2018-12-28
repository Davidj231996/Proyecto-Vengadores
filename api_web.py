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
        "GET":{
            "CuentaNoticias":{
                "ruta":"/cuentaNoticias",
                "valor": "El valor de la cantidad de noticias"
            },
            "MostrarNoticiasCategoria":{
                "ruta":"/mostrarNoticiasCategoira<?categoria=valor2>",
                "valor": "{Numero:<muestra el numero de noticias de esa categoria>}"
            },
            "Status":{
                "ruta":"/status",
                "valor":"OK"
        },
        "POST":{
            "CrearNoticia":
               { "ruta": "/crearNoticia",
                 "parametros post": "titulo=valor1, descripcion=valor2, categoria=valor3",
                 "valor": "Noticias:<La cantidad aumenta>"}
        },
        "PUT":{
            "EditarNoticia":
                {"ruta": "/editarNoticia",
                "parametros put":"titulo=valor1, descripcion=valor2, categoria=valor3, indice=valor4",
                "valor": "{Editado: True o False}"}            }
        },
        "DELETE":{
            "EliminarNoticia":{
                "ruta":"/eliminarNoticia",
                "parametros delete":"indice=valor1",
                "valor": "{El valor de la cantidad disminuye}"
            }    
        }
    })

#GET
@app.route("/status")
def status():
    return jsonify({"status":"OK"})

@app.route("/cuentaNoticias")
def CuentaNoticias():
    return jsonify(n.cuentaNoticias())

@app.route("/mostrarNoticiasCategoira")
def MostrarNoticiasCategoria():
    if request.args.get('categoria'):
        categoria=request.args.get('categoria')
    else:
        return jsonify(Numero=0)
    return jsonify(Numero=n.mostrarNoticiasCategoria(categoria))

#POST
@app.route("/crearNoticia", methods=["POST"])
def CrearNoticia():
    if request.method=="POST":
        json_data = request.get_json()
        titulo=json_data['titulo']
        descripcion=json_data['descripcion']
        categoria=json_data['categoria']
    return jsonify(Noticias=n.crear_Noticia(titulo,descripcion,categoria))

#PUT
@app.route("/editarNoticia", methods=["PUT"])
def EditarNoticia():
    if request.method=="PUT":
        json_data=request.get_json()
        titulo=json_data['titulo']
        descripcion=json_data['descripcion']
        categoria=json_data['categoria']
        indice=json_data['indice']
    return jsonify(Editado=n.editarNoticia(titulo,descripcion,categoria,indice))

#DELETE
@app.route("/eliminarNoticia")
def EliminarNoticia():
    if request.method=="DELETE":
        json_data=request.get_json()
        indice=json_data['indice']
    return jsonify(n.eliminarNoticia(indice))

@app.errorhandler(404)
def page_not_found(error):
  		return "Página no encontrada", 404

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
