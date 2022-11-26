from Modelos.Candidato import Candidato
from Modelos.PartidoPolitico import PartidoPolitico
from Modelos.Resultados import Resultados
from Repositorios.CandidatoRepositorio import CandidatoRepositorio
from Repositorios.PartidoPoliticoRepositorio import PartidoPoliticoRepositorio
from Repositorios.ResultadosRepositorio import ResultadosRepositorios

class ResultadosController():
    def __init__(self):
        print("Creando el controlador de Resultados")
        self.CandidatoRepositorio = CandidatoRepositorio()
        self.PartidoPoliticoRepositorio = PartidoPoliticoRepositorio()
        self.ResultadosRepositorios = ResultadosRepositorios()


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
        candidato = Candidato(self.CandidatoRepositorio.findByIdCedula(id_cedula))
        partido = PartidoPolitico(self.PartidoPoliticoRepositorio.findByIdCodigo(id_codigo))
        resultado.candidato = candidato
        resultado.partido = partido
        return self.ResultadosRepositorios.save(resultado)

    def index(self):
        print("mostrando todos los resultados")
        return self.ResultadosRepositorios.findAll()

    def delete(self, id):
        print("borrando el resultado: ", id)
        return ResultadosRepositorios.delete(id)

    def show(self, id):
        print("mostrando los resultado: ", id)
        resultado = ResultadosRepositorios.findByIdR(id)
        return resultado.__dict__

    def consultarInscritosCandidatos(self, id):
        print("Consulatando Inscritos de los candidatos")
        return self.ResultadosRepositorios.getInscritosCandidato(id)

    def consultarMayorCandidato(self):
        print("Consultando el canidato mas votado")
        return self.ResultadosRepositorios.getMayorVotacion()

    def consultarPromedioCAndidato(self, id):
        print("Consultando promedio candidatos")
        return self.ResultadosRepositorios.getVotacionPromedio(id)

    def consulatrSumatoriaVotos(self, id):
        print("Consultando la sumatoria de los votos")
        return self.ResultadosRepositorios.getNSumatoriaVotos(id)