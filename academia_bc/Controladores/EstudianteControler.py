'''Estos controladores tendran la logica del programa (metodos) por cada clase de Modelos'''
from Modelos.Estudiante import Estudiante
from Repositorio.EstudianteRepositorio import EstudianteRepositorio

class EstudianteControler():
    def __int__(self):
        print("Construyendo Controlador de Estudiante")
        self.estudianteRepositorio = EstudianteRepositorio()


    'Listado'
    def index(self):
        print("Listado de todos los Estudiante")
        return self.estudianteRepositorio.findAll()

    'Creacion'
    def create(self, unEstudiante):
        print("Creando el estudiante")
        estudiante = Estudiante(unEstudiante)
        return self.estudianteRepositorio.save(estudiante)


    'Borrado'
    def delete(self, id):
        print("Borrando estudiante: ", id)
        return self.estudianteRepositorio.delete(id)

    'Actualizacion'
    def update(self, id, estudiante):
        print("Actualizando rl estudiante: ", id)
        estActual = (self.estudianteRepositorio.findById(id))
        estActual.cedula = estudiante["cedula"]
        estActual.nombre = estudiante["nombre"]
        estActual.apellido = estudiante["apellido"]
        return self.estudianteRepositorio.save(estActual)

    'Consulta'
    def show(self, id):
        print("Consultando el estudiante: ", id)
        estudiante = Estudiante(self.estudianteRepositorio.findById(id))

        estudiante = {
            "_id": id,
            "cedula": "987",
            "nombre": "Estudiante",
            "apellido": "De prueba"
        }
        return estudiante