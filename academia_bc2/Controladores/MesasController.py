from Modelos.Mesas import Mesas
from Repositorios.MesasRepositorio import MesasRepositorio


class MesasController():
    def __init__(self):
        print("Construyendo controlador de las Mesas")
        self.MesasRepositorio = MesasRepositorio()



    #lISTADO
    def index(self):
        print("Listado de todas las Mesas")
        return self.MesasRepositorio.findAll()

    #CREACIO
    def create(self, unaMesa):
        print("Creando un candidato")
        mesa= Mesas(unaMesa)
        return self.MesasRepositorio.save(mesa)
        #return candidato.__dict__ # __dict__ Esta funcion nos ayuda a que nos retirne una estructura tipo json

    #BORRADO
    def delete(self, id_numero):
        print("borrando estudiante: ", id_numero)
        return self.MesasRepositorio.deletMesa(id_numero)

    #ACTUALIZAR
    def update(self, id_numero, mesa):
        print("Actualizando al candidato: ", id_numero)
        mesaActu = Mesas(self.MesasRepositorio.findByIdNumero(id_numero))
        mesaActu.id_numero = mesa["id_numero"]
        mesaActu.candidatosInscritos = mesa["candidatosInscritos"]
        return self.MesasRepositorio.save(mesaActu) # Se retorna con un save para que en caso de que no exista este se cree

    #CONSULTAR
    def show(self, id_numero):
        print("Consultando candidato: ", id_numero)
        mesa = Mesas(self.MesasRepositorio.findByIdNumero(id_numero))
        return mesa.__dict__