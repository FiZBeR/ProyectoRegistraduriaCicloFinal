'''Estos controladores tendran la logica del programa (metodos) por cada clase de Modelos'''
from Modelos.Estudiante import Estudiante

class EstudianteControler():
    def __int__(self):
        print("Construyendo Controlador de Estudiante")

    'Listado'
    def index(self):
        print("Listado de todos los Estudiante")
        estudiante = {
            "_id": "1",
            "cedula": "987",
            "nombre": "Estudiante",
            "apellido": "De prueba"
        }
        return [estudiante]

    'Creacion'
    def create(self, unEstudiante):
        print("Creando el estudiante")
        estudiante = Estudiante(unEstudiante)
        return estudiante.__dict__


    'Borrado'
    def delete(self, id):
        print("Borrando estudiante: ", id)
        return {"Borrando estudiante: ": id}

    'Actualizacion'
    def update(self, id, estudiante):
        print("Actualizando rl estudiante: ", id)
        est = Estudiante(estudiante)
        return est.__dict__

    'Consulta'
    def show(self, id):
        print("Consultando el estudiante: ", id)
        estudiante = {
            "_id": id,
            "cedula": "987",
            "nombre": "Estudiante",
            "apellido": "De prueba"
        }
        return estudiante