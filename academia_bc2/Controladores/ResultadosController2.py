from Modelos.Candidato import Candidato
from Modelos.PartidoPolitico import PartidoPolitico
from Modelos.Resultados import Resultados
from Repositorios.CandidatoRepositorio import CandidatoRepositorio
from Repositorios.PartidoPoliticoRepositorio import PartidoPoliticoRepositorio
from Repositorios.ResultadosRepositorio import Resultadosrepositorios

class ResultadosController():
    def __init__(self):
        print("Creando el controlador de Resultados")
        self.repoCandidato = CandidatoRepositorio
        self.repoPartido = PartidoPoliticoRepositorio
        self.repoResultados = Resultadosrepositorios

    def findByIdR(self, id):
        laColeccion = self.baseDatos[self.coleccion]
        x = laColeccion.find_one({"id": id})

        if x == None:
            x = {}
        else:
            x["_id"] = x["_id"].__str__()
        return x

    def create(self, dataResultados, id_cedula, id_codigo):
        resultado = Resultados(dataResultados)
        candidato = Candidato(self.repoCandidato.findByIdCedula(id_cedula))
        partido = PartidoPolitico(self.repoPartido.findByIdCodigo(id_codigo))
        resultado.candidato = candidato
        resultado.partido = partido
        return self.repoResultados.save(resultado)

    def index(self):
        print("mostrando todos los resultados")
        return self.ResultadosRepositorio.findAll()

    def delete(self, id):
        print("borrando el resultado: ", id)
        return Resultadosrepositorios.delete(id)

    def show(self, id_cedula):
        print("mostrando los resultado: ", id)
        resultado = Resultadosrepositorios.findByIdR(id_cedula)
        return resultado.__dict__

    def consultarInscritosCandidatos(self, id_cedula):
        print("Consulatando Inscritos de los candidatos")
        return self.repoResultados.getInscritosCandidato(id_cedula)

    def consultarMayorCandidato(self):
        print("Consultando el canidato mas votado")
        return self.repoResultados.getMayorVotacion()

    def consultarPromedioCAndidato(self, id_cedula):
        print("Consultando promedio candidatos")
        return self.repoResultados.getVotacionPromedio(id_cedula)

    def consulatrSumatoriaVotos(self, id_cedula):
        print("Consultando la sumatoria de los votos")
        return self.repoResultados.getNSumatoriaVotos(id_cedula)