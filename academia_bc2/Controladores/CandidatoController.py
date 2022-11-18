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
        return self.CandidatoRepositorio.save(candidato)
        return candidato.__dict__ # __dict__ Esta funcion nos ayuda a que nos retirne una estructura tipo json

    #BORRADO
    def delete(self, cedula):
        print("borrando estudiante: ", cedula)
        return self.CandidatoRepositorio.delete(cedula)

    #ACTUALIZAR
    def update(self, cedula, candidato):
        print("Actualizando al candidato: ", cedula)
        candiActu = Candidato(self.CandidatoRepositorio.findById(cedula))
        candiActu.partido = candidato["partido"]
        candiActu.numero_de_resolucion = candidato["numero de resolucion"]
        candiActu.cedula = candidato["cedula"]
        candiActu.nombre = candidato["nombre"]
        candiActu.apellido = candidato["apellido"]
        return self.CandidatoRepositorio.save(candiActu) # Se retorna con un save para que en caso de que no exista este se cree

    #CONSULTAR
    def show(self, cedula):
        print("Consultando candidato: ", cedula)
        candidato = Candidato(self.CandidatoRepositorio.findById(cedula))
        return candidato.__dict__

        #Relacion Partido Politico y Candidato clase del 21 minuto del 30 al 40 Explicacion 
    def asignarPartidoPolitico(self, id_cedula, id_codigo):
        candidaActu = Candidato(self.CandidatoRepositorio.findById(id_cedula))#Obtener candidato
        PartiActual = PartidoPolitico(self.PartidoPoliticoRepositorio.findById(id_codigo))#Obtener partido
        candidaActu.PartidoPolitico = PartiActual #Asignar Partido
        return self.CandidatoRepositorio.save(candidaActu)







