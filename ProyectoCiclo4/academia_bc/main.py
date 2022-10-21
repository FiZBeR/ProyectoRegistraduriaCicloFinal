from flask import Flask
from flask import jsonify
from flask import request
from flask_core import CORS
import json
from waitress import server, serve

app=Flask(__name__)
cors = CORS(app)


from Controladores.EstudianteControler import EstudianteControler
controladorEstudiante = EstudianteControler()

    #Micro servicio de Creacion
@app.route("/estudiantes",methods=['POST'])
def crearEstudiante():
    datos = request.get_json()
    json = controladorEstudiante.create(datos)
    return jsonify(json)

       #Micro servicio de Listado
@app.route("/estudiantes",methods=['GET'])
def getEstudiante():
    json = controladorEstudiante.index()
    return jsonify(json)

       #Micro servicio de Consulta
@app.route("estudiantes/<string:id>",methods=['GET'])
def getEstudiante(id):
    json = controladorEstudiante.show()
    return jsonify(json)

       #Micro servicio de Actualizacion
@app.route("estudiantes/<string:id>",methods=['PUT'])
def actualizarEstudiante(id):
    datos = request.get_json()
    json = controladorEstudiante.update(id,datos)
    return jsonify(json)

      #Micro servicio de Borrado
@app.route("estudiantes/<string:id>",methods=['DELETE'])
def borrarEstudiante(id):
    json = controladorEstudiante.delete(id)
    return jsonify(json)

@app.route("/",methods=['GET'])
def msPrueba():
    json = {}
    json["message"] = "Mi primer micro servico con Flask"
    return jsonify(json)

def cargueConfigFile():
    with open('config.json') as file:
        datos = json.load(file)
    return datos


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Grupo 32')
    configData = cargueConfigFile()
    print("Servidor Ejecutandose ..... en http//:"+configData["url-backend"]+":"+str(configData["port"]))
    serve(app, host=configData["url-backend"], port=configData["port"])
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
