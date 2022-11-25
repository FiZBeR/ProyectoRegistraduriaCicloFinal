from Repositorios.RepositorioInterfase2 import RepositorioInterface
from Modelos.Mesas import Mesas

class MesasRepositorio(RepositorioInterface[Mesas]):
    def findByIdNumero(self, id_numero):
        laColeccion = self.baseDatos[self.coleccion]
        x = laColeccion.find_one({"id_numero": id_numero})

        if x == None:
            x = {}
        else:
            x["_id"] = x["_id"].__str__()
        return x

    def deletMesa(self, id_numero):
        laColeccion = self.baseDatos[self.coleccion]
        cuenta = laColeccion.delete_one({"id_numero": id_numero}).deleted_count
        return {"deleted_count": cuenta}