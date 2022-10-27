'''Al hacer esto le daremos el codigo a las bases de datos para realizar el CRUD'''
import pymongo
import certifi
from bson import DBRef
from bson.objectid import ObjectId
from typing import TypeVar, Generic, List, get_args, get_origin
import json

'La declaracion del Objeto T y es que el que recibe nuestro repositorio Interface, es una manera en la que le deciomos'''
'que va a recibir un objeto y decirle al programa que la declaracion de cad objeto es un tipo estandar y aplica para todos'''
'los modelos que se comporten de esa forma '''
T = TypeVar('T')
class RepositorioInterface(Generic[T]):

    def __init__(self):
        ca = certifi.where()
        configData = self.cargueConfigFile()
        clientDb = pymongo.MongoClient(configData["bd=connection"], tlsCAFile=ca)
        self.baseDatos = clientDb[configData["bd-name"]]
        clase = get_args(self.__orig_bases__[0])
        self.coleccion = clase[0].__name__.lower()


    def cargueConfigFile(self):
        with open('config.json') as file:
            datos = json.load(file)
        return datos

#metodos

    def save(self, obj: T):
        return ""

    def update(self, id, obj: T):
        return ""

    def delete(self, id):
        return {"Borrando estudiante: ": id}


    def findAll(self): #Este metodo se utiliza mucho y sirve para mostrar todo
        estudiante = {
            "_id": "1",
            "cedula": "987",
            "nombre": "Estudiante",
            "apellido": "De prueba"
        }
        return [estudiante]

    def findById(self, id): #Este metodo me consulta uno solo teniendo como referencia el ID
        return ""


