# Departamento = Partidos
from Modelos.PartidoPolitico import PartidoPolitico
from Repositorios.CandidatoRepositorio import CandidatoRepositorio
from Repositorios.PartidoPoliticoRepositorio import PartidoPoliticoRepositorio


class PartidoPoliticoController():
    def __init__(self):
        print("Construyendo el controlador de partidos politicos")
        self.PartidoPoliticoRepositorio = PartidoPoliticoRepositorio


    def index(self):
        print("Mostrando todos los Partidos Politicos")
        return self.PartidoPoliticoRepositorio.findAll()


    def create(self, unPartido):
        print("Creando Un partido")
        unPPolitico = PartidoPolitico(unPartido)
        return self.PartidoPoliticoRepositorio.save(unPPolitico)


    def delete(self, codigo):
        print("Borrando al partio Politico: ", codigo)
        return PartidoPoliticoRepositorio.delete(codigo)


    def update(self, codigo, partidopolitico):
        print("Actualizando al partido politico: ", codigo)
        ppolitico = PartidoPolitico(self.PartidoPoliticoRepositorio.findById(codigo))
        ppolitico.nombre = partidopolitico["nombre"]
        ppolitico.lema = partidopolitico["lema"]
        ppolitico.codigo = partidopolitico["codigo"]
        return self.PartidoPoliticoRepositorio.save(ppolitico)


    def show(self, codigo):
        print("Consultando al partido: ",codigo)
        partidopolitico = PartidoPolitico(self.PartidoPoliticoRepositorio.findById(codigo))
        return partidopolitico.__dict__



