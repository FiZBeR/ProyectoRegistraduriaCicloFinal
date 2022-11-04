from Repositorio.RepositorioInterface import RepositorioInterface
from Modelos.Inscripcion import Inscripcion
from bson import ObjectId


class InscripcionRepositorio(RepositorioInterface[Inscripcion]):

    def getInscritosAmateria(self, id_materia):
        consulta = {"materia.$id": ObjectId(id_materia)}
        return self.query(consulta)

    def getMejorNotaEnMateria(self):
        consulta = {
            "$group":{
                "_id": "$materia",
                "max": {
                    "$max": "$nota_final"
                },
                "doc": {
                    "$first": "$$ROOT"
                }
            }
        }
        pipeline = [consulta]
        return self.queryAggregation(pipeline) #lo que hace esta funcion es exclusivo o es variable

    def getNotaPromedio(self, id_materia):
        consulta1 = {
            "$match" : {"materia.$id": ObjectId(id_materia)}
        }
        consulta2 = {
            "$group" : {
                "_id": "$materia",
                "promedio": {
                    "$avg": "$nota_final"
                }
            }
        }

        pipeline = [consulta1, consulta2]
        return self.queryAggregation(pipeline)

    def getNSumatoriaNota(self, id_materia):
        consulta1 = {
            "$match" : {"materia.$id": ObjectId(id_materia)}
        }
        consulta2 = {
            "$group" : {
                "_id": "$materia",
                "promedio": {
                    "$sum": "$nota_final"
                }
            }
        }

        pipeline = [consulta1, consulta2]
        return self.queryAggregation(pipeline)
    # Estructuta
    def funcion(self, parametro): #se define la funcion y sus parametros
        consulta = {} #Armamos consulta a la base de datos
        return self.query(consulta) #repositorio ejecuta la consulta