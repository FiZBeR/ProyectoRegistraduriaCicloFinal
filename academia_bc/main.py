import pymongo
import certifi
from flask import Flask
from flask import jsonify #para que funciona
from flask import request
from flask_cors import CORS
import json
from waitress import server, serve

app=Flask(__name__)
cors = CORS(app)

#Agregar base de datos

ca = certifi.where() #para que funciona
clientDb = pymongo.MongoClient("mongodb+srv://CristianNew3:Ozzy19780Zeppelin@cluster0.h1ic9da.mongodb.net/Cliclo4A?retryWrites=true&w=majority", tlsCAFile=ca)

bd = clientDb.test
print(bd)

base = clientDb["academia-c4"]
print(base.list_collection_names())

#Controladores
from Controladores.EstudianteControler import EstudianteControler
from Controladores.MateriaControlador import MateriaControlador
from Controladores.InscripcionControlador import InscripcionControlador
controladorEstudiante = EstudianteControler()
controladorMateria = MateriaControlador()
controladorInscripcion = InscripcionControlador()


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

@app.route("/materia/<string:id_materia>/departamento/<string:id_departamento>",methods=['PUT'])
def asignarDepartamento(id_materia, id_departamento):
    json = controladorMateria.asignarDepartamento(id_materia, id_departamento)
    return jsonify(json)

@app.route("/inscripciones/estudiante/<string:id_estudiante>/materia/<string:id_materia>",methods=['POST'])
def crearInscripcion(id_estudiante, id_materia):
    datos = request.get_json()
    json = controladorInscripcion.create(datos, id_estudiante, id_materia)
    return jsonify(json)

@app.router("/inscripciones/materia/<string:id_materia>", methods=['GET'])
def isncritosEnMateria(id_materia):
    json = controladorInscripcion.consultarInscritosPorMateria(id_materia)
    return jsonify(json)

@app.router("/inscripciones/materia", methods=['GET'])
def mejorNotaEnMateria(id_materia):
    json = controladorInscripcion.consultarMejorNotaEnMateria(id_materia)
    return jsonify(json)

@app.router("/inscripciones/Promedio_notas/<string:id_materia>", methods=['GET'])
def mejorNotaEnMateria(id_materia):
    json = controladorInscripcion.consultarNotaPromedio(id_materia)
    return jsonify(json)

@app.router("/inscripciones/Sumatoria_notas/<string:id_materia>", methods=['GET'])
def mejorNotaEnMateria(id_materia):
    json = controladorInscripcion.consultarSumatoriaNotas(id_materia)
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
