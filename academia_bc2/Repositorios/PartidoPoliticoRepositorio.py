from Repositorios.RepositorioInterfase2 import RepositorioInterface
from Modelos.PartidoPolitico import PartidoPolitico
class PartidoPoliticoRepositorio(RepositorioInterface[PartidoPolitico]):
    pass
    def findByIdCodigo(self, id_codigo):
        laColeccion = self.baseDatos[self.coleccion]
        x = laColeccion.find_one({"id_codigo": id_codigo})

        if x == None:
            x = {}
        else:
            x["_id"] = x["_id"].__str__()
        return x

    def deletCodigo(self, id_codigo):
        laColeccion = self.baseDatos[self.coleccion]
        cuenta = laColeccion.delete_one({"id_codigo": id_codigo}).deleted_count
        return {"deleted_count": cuenta}


