from Repositorios.RepositorioInterfase2 import RepositorioInterface
from Modelos.Resultados import Resultados
from bson import ObjectId

class ResultadosRepositorios(RepositorioInterface[Resultados]):
    pass



    def getInscritosCandidato(self, id_cedula):
        consulta = {"candidato.$id": ObjectId(id_cedula)}
        return self.query(consulta)


    def getMayorVotacion(self):
        consulta = {
            "$group": {
                "_id": "$mesas",
                "max": {
                    "$max": "$candidatos_inscritos"
                },
                "doc": {
                    "$first": "$$ROOT"
                }
            }
        }
        pipeline = [consulta]
        return self.queryAggregation(pipeline)  # lo que hace esta funcion es exclusivo o es variable


    def getVotacionPromedio(self, id_cedula):
        consulta1 = {
            "$match": {"Candidato.$id": ObjectId(id_cedula)}
        }
        consulta2 = {
            "$group": {
                "_id": "$id_cedula",
                "promedio": {
                    "$avg": "$nota_final"
             }
            }
        }

        pipeline = [consulta1, consulta2]
        return self.queryAggregation(pipeline)


    def getNSumatoriaVotos(self, id_cedula):
        consulta1 = {
            "$match": {"Candidato.$id": ObjectId(id_cedula)}
        }
        consulta2 = {
            "$group": {
                "_id": "$cedula",
                "promedio": {
                    "$sum": "$nota_final"
                }
            }
        }

        pipeline = [consulta1, consulta2]
        return self.queryAggregation(pipeline)


    # Estructuta
    def funcion(self, parametro):  # se define la funcion y sus parametros
        consulta = {}  # Armamos consulta a la base de datos
        return self.query(consulta)  # repositorio ejecuta la consulta