from Repositorios.RepositorioInterfase2 import RepositorioInterface
from Modelos.Candidato import Candidato
from typing import TypeVar

T = TypeVar('T')
class CandidatoRepositorio(RepositorioInterface[Candidato]):
    def findByIdCedula(self, id_cedula):
        laColeccion = self.baseDatos[self.coleccion]
        x = laColeccion.find_one({"id_cedula": id_cedula})

        if x == None:
            x = {}
        else:
            x["_id"] = x["_id"].__str__()
        return x

    def deletCedula(self, id_cedula):
        laColeccion = self.baseDatos[self.coleccion]
        cuenta = laColeccion.delete_one({"id_cedula": id_cedula}).deleted_count
        return {"deleted_count": cuenta}

    '''def updateCedula(self, id_cedula, item: T):
        id_cedula = id_cedula
        laColeccion = self.baseDatos[self.coleccion]
        delattr(item, "id_cedula")
        item = item.__dict__
        updateItem = {"$set": item}
        x = laColeccion.update_one({"id_cedula": id_cedula}, updateItem)
        return {"updated_count": x.matched_count}'''


