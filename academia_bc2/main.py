import pymongo
import certifi
from flask import Flask
from flask import jsonify #Es para el manejo de los json y haga el mapeo de estos
from flask import request
from flask_cors import CORS
import json
from waitress import serve

#importar los controladores para las exposiciones
from Controladores.CandidatoController import CandidatoController
from Controladores.PartidosPoliticosController import PartidoPoliticoController
from Controladores.ResultadosController2 import ResultadosController

controladorCandidato = CandidatoController()
controladorPartidoPoli = PartidoPoliticoController()
controladorResultados = ResultadosController

#
app=Flask(__name__)
cors= CORS(app)

#Conexion Base de Datos
ca = certifi.where()
clienteDb = pymongo.MongoClient("mongodb+srv://CristianNew3:Ozzy19780Zeppelin@cluster0.h1ic9da.mongodb.net/ProyectoCiclo4?retryWrites=true&w=majority", tlsCAFile=ca)
Db = clienteDb.test
print(Db)

base = clienteDb["ProyectoCiclo4"]
print(base.list_collection_names())



#Ejemplos de Expocision de microservicios----------------Creacion de Candidatos---------------------------------------------------------------
from Controladores.CandidatoController import CandidatoController
controladorCandidato = CandidatoController()

# Microservicio de Crearcion
@app.route("/candidatos", methods=['POST'])
def crearCandidato():
    datos = request.get_json()
    json = controladorCandidato.create(datos)
    return jsonify(json)

# Microservicio de Listado
@app.route("/candidatos", methods=['GET'])
def getCandidatos():
    json = controladorCandidato.index()
    return jsonify(json)

# Microservicio de Borrar
@app.route("/candidatos/<string:id_cedula>", methods=['DELETE'])
def borrarCandidato(id_cedula):
    json = controladorCandidato.deleteCedula(id_cedula)
    return jsonify(json)

# Microservicio de Actualizar
@app.route("/candidatos/<string:id_cedula>", methods=['PUT'])
def actualizarCandidato(id_cedula):
    datos = request.get_json()
    json = controladorCandidato.update(id_cedula, datos)
    return jsonify(json)

# Microservicio de Consulta
@app.route("/candidatos/<string:id_cedula>", methods=['GET'])
def getCandidato(id_cedula):
    json = controladorCandidato.show(id_cedula)
    return jsonify(json)


#Creacion de Partido Politico---------------------------------------------------------------

from Controladores.PartidosPoliticosController import PartidoPoliticoController
controladorPartidoPolitico = PartidoPoliticoController()

#Crearcion
@app.route("/partidopolitico", methods=['POST'])
def crearPartido():
    datos = request.get_json()
    json = controladorPartidoPolitico.create(datos)
    return jsonify(json)

#Listado
@app.route("/partidopolitico", methods=['GET'])
def getPartidos():
    json = controladorPartidoPolitico.index()
    return jsonify(json)

#Borrar
@app.route("/partidopolitico/<string:id_codigo>", methods=['DELETE'])
def borrarPartido(id_codigo):
    json = controladorPartidoPolitico.delete(id_codigo)
    return jsonify(json)

#Actualizar
@app.route("/partidopolitico/<string:id_codigo>", methods=['PUT'])
def actualizarPartido(id_codigo):
    datos = request.get_json()
    json = controladorPartidoPolitico.update(id_codigo, datos)
    return jsonify(json)

#Consulta
@app.route("/partidopolitico/<string:id_codigo>", methods=['GET'])
def getPartido(id_codigo):
    json = controladorPartidoPolitico.show(id_codigo)
    return jsonify(json)

#Creacion de Mesas---------------------------------------------------------------

from Controladores.MesasController import MesasController
controladorMesas = MesasController()

#Crearcion
@app.route("/mesas", methods=['POST'])
def crearMesas():
    datos = request.get_json()
    json = controladorMesas.create(datos)
    return jsonify(json)

#Listado
@app.route("/mesas", methods=['GET'])
def getMesas():
    json = controladorMesas.index()
    return jsonify(json)

#Borrar
@app.route("/mesas/<string:id_numero>", methods=['DELETE'])
def borrarMesas(id_numero):
    json = controladorMesas.delete(id_numero)
    return jsonify(json)

#Actualizar
@app.route("/mesas/<string:id_numero>", methods=['PUT'])
def actualizarMesas(id_numero):
    datos = request.get_json()
    json = controladorMesas.update(id_numero, datos)
    return jsonify(json)

#Consulta
@app.route("/mesas/<string:id_numero>", methods=['GET'])
def getMesa(id_numero):
    json = controladorMesas.show(id_numero)
    return jsonify(json)

#Creacion de Resultados---------------------------------------------------------------

from Controladores.ResultadosController2 import ResultadosController
controladorResultados = ResultadosController()

#Crearcion
@app.route("/resultados", methods=['POST'])
def crearResultados():
    datos = request.get_json()
    json = controladorResultados.create(datos)
    return jsonify(json)

#Listado
@app.route("/resultados", methods=['GET'])
def getResultados():
    json = controladorResultados.index()
    return jsonify(json)

#Borrar
@app.route("/resultados/<string:id>", methods=['DELETE'])
def borrarResultados(id):
    json = controladorResultados.delete(id)
    return jsonify(json)

#Actualizar
@app.route("/resultados/<string:id>", methods=['PUT'])
def actualizarResultados(id):
    datos = request.get_json()
    json = controladorResultados.update(id, datos)
    return jsonify(json)

#Consulta
@app.route("/resultados/<string:id>", methods=['GET'])
def getResultado(id):
    json = controladorResultados.show(id)
    return jsonify(json)
#-----------------------------------------------------------------------------------------------------------------
#Exponer Servicios

@app.route("/partidopoliticos/<string:id_codigo>/candidato/<string:id_cedula>", methods=['PUT'])
def asignarpartidoPoli(id_codigo, id_cedula):
    json = controladorCandidato.asignarPartidoPolitico(id_cedula, id_codigo)
    return jsonify(json)

@app.route("/Resultado/candidato/<string:id_cedula>/PartidoPolitico/<string:id_codigo>", methods=['POST'])
def crearResultado(id_cedula, id_codigo):
    datos = request.get_json()
    json = controladorResultados.create(datos, id_cedula, id_codigo)
    return jsonify(json)

# Microservisios de consultas especiales----------------------------------------------------------

@app.route("/resultados/candidato/<string:id_cedula>", methods=['GET'])
def isncritosEnCandiadtos(id_cedula):
    json = controladorResultados.consultarInscritosCandidatos(id_cedula)
    return jsonify(json)

@app.route("/resultados/candidato", methods=['GET'])
def mejorVotacionEnCandidato(id_cedula):
    json = controladorResultados.consultarMayorCandidato(id_cedula)
    return jsonify(json)

@app.route("/resultados/Promedio_notas/<string:id_cedula>", methods=['GET'])
def promediocandidatos(id_cedula):
    json = controladorResultados.consulatrSumatoriaVotos(id_cedula)
    return jsonify(json)

@app.route("/inscripciones/Sumatoria_notas/<string:id_cedula>", methods=['GET'])
def mayorSumatoria(id_cedula):
    json = controladorResultados.consulatrSumatoriaVotos(id_cedula)
    return jsonify(json)

#Pruebas-----------------------------------------------------------------------------------------------------------------------------------------
@app.route("/", methods=['GET'])
def msPrueba():
    json = {}
    json["mensaje"] = "Mi primer Micro Servicio con Flask"
    return jsonify(json)

#
def cargueConfigfile():
    with open('config.json') as file:
        datos = json.load(file)
    return datos

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, grupo 32')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Hi Cristian')
    configData= cargueConfigfile()
    print('servidor ejecutandose ..... en: http://'+configData["url-backend"] + ":" + str(configData["port"]))
    serve(app,host=configData["url-backend"],port=configData["port"])
    #Esta linea junto a la dependencia de waitress nos ayuda a arrancar el servidor de la app en el host que
    #declaramos en el archivo configData al igual que el puerto

