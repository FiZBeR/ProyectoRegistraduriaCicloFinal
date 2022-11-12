import pymongo
import certifi
from flask import Flask
from flask import jsonify #Es para el manejo de los json y haga el mapeo de estos
from flask import request
from flask_cors import CORS
import json
from waitress import serve

#
app=Flask(__name__)
cors= CORS(app)




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

