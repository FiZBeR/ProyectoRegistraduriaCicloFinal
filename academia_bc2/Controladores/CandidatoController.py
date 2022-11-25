# Materia = Candidato
from Modelos.Candidato import Candidato
from Modelos.PartidoPolitico import PartidoPolitico
from Repositorios.PartidoPoliticoRepositorio import PartidoPoliticoRepositorio
from Repositorios.CandidatoRepositorio import CandidatoRepositorio

class CandidatoController():
    def __init__(self):
        print("Construyendo controlador de Candidato")
        self.CandidatoRepositorio = CandidatoRepositorio()
        self.PartidoPoliticoRepositorio = PartidoPoliticoRepositorio()



    #lISTADO
    def index(self):
        print("Listado de todos los candidatos")
        return self.CandidatoRepositorio.findAll()

    #CREACIO
    def create(self, unCandidato):
        print("Creando un candidato")
        candidato = Candidato(unCandidato)
        print(candidato)
        return self.CandidatoRepositorio.save(candidato)
        return candidato.__dict__
        # __dict__ Esta funcion nos ayuda a que nos retirne una estructura tipo json

    #BORRADO
    def deleteCedula(self, id_cedula):
        print("borrando estudiante: ", id_cedula)
        return self.CandidatoRepositorio.deletCedula(id_cedula)

    #ACTUALIZAR
    def update(self, id_cedula, candidato):
        print("Actualizando al candidato: ", id_cedula)
        candiActu = Candidato(self.CandidatoRepositorio.findByIdCedula(id_cedula))
        candiActu.partido = candidato["partido"]
        candiActu.numero_de_resolucion = candidato["numero de resolucion"]
        candiActu.id_cedula = candidato["id_cedula"]
        candiActu.nombre = candidato["nombre"]
        candiActu.apellido = candidato["apellido"]
        return self.CandidatoRepositorio.save(candiActu) # Se retorna con un save para que en caso de que no exista este se cree

    #CONSULTAR
    def show(self, id_cedula):
        print("Consultando candidato: ", id_cedula)
        candidato = Candidato(self.CandidatoRepositorio.findByIdCedula(id_cedula))
        return candidato.__dict__


    def asignarPartidoPolitico(self, id_cedula, id_codigo):
        candidaActu = Candidato(self.CandidatoRepositorio.findByIdCedula(id_cedula))#Obtener candidato
        PartiActual = PartidoPolitico(self.PartidoPoliticoRepositorio.findByIdCodigo(id_codigo))#Obtener partido
        candidaActu.PartidoPolitico = PartiActual #Asignar Partido
        return self.CandidatoRepositorio.save(candidaActu)







