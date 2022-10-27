from Modelos.Materia import Materia
from Repositorio.MateriaRepositorio import MateriaRepositorio

class MateriaControler():
    def __int__(self):
        print("Construyendo Controlador de Estudiante")
        self.materiaRepositorio = MateriaRepositorio()


    'Listado'
    def index(self):
        print("Listado de todos los Estudiante")
        return self.materiaRepositorio.findAll()

    'Creacion'
    def create(self, unaMateria):
        print("Creando el estudiante")
        materia = Materia(unaMateria)
        return self.materiaRepositorio.save(materia)


    'Borrado'
    def delete(self, id):
        print("Borrando estudiante: ", id)
        return self.materiaRepositorio.delete(id)

    'Actualizacion'
    def update(self, id, materia):
        print("Actualizando la materia: ", id)
        matActual = (self.materiaRepositorio.findById(id))
        matActual.nombre = materia["nombre"]
        matActual.creditos = materia["creditos"]
        return self.materiaRepositorio.save(matActual)

    'Consulta'
    def show(self, id):
        print("Consultando el estudiante: ", id)
        materia = Materia(self.materiaRepositorio.findById(id))
        return materia.__dict__