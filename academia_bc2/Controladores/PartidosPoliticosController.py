# Departamento = Partidos
from Modelos.Candidato import Candidato
from Modelos.PartidoPolitico import PartidoPolitico
from Repositorios.CandidatoRepositorio import CandidatoRepositorio
from Repositorios.PartidoPoliticoRepositorio import PartidoPoliticoRepositorio


class PartidoPoliticoController():
    def __init__(self):
        print("Construyendo el controlador de partidos politicos")
        self.PartidoPoliticoRepositorio = PartidoPoliticoRepositorio()


    def index(self):
        print("Mostrando todos los Partidos Politicos")
        return PartidoPoliticoRepositorio.findAll()

    def create(self, unPartido):
        print("Creando un Partido")
        partido = PartidoPolitico(unPartido)
        print(partido)
        return self.PartidoPoliticoRepositorio.save(partido)
        return partido.__dict__


    def delete(self, id_codigo):
        print("Borrando al partio Politico: ", id_codigo)
        return PartidoPoliticoRepositorio.deletCodigo(id_codigo)

    def update(self, id_codigo, partidopolitico):
        print("Actualizando al partido politico: ", id_codigo)
        ppolitico = PartidoPolitico(self.PartidoPoliticoRepositorio.findByIdCodigo(id_codigo))
        ppolitico.nombre = partidopolitico["nombre"]
        ppolitico.lema = partidopolitico["lema"]
        ppolitico.id_codigo = partidopolitico["id_codigo"]
        return self.PartidoPoliticoRepositorio.save(ppolitico)

    def show(self, id_codigo):
        print("Consultando al partido: ", id_codigo)
        partidopolitico = PartidoPolitico(self.PartidoPoliticoRepositorio.findByIdCodigo(id_codigo))
        return partidopolitico.__dict__
