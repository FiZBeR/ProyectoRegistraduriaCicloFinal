from Modelos.Materia import Materia
from Modelos.Estudiante import Estudiante
from Modelos.Inscripcion import Inscripcion
from Repositorio.EstudianteRepositorio import EstudianteRepositorio
from Repositorio.MateriaRepositorio import MateriaRepositorio
from Repositorio.InscripcionRepositorio import InscripcionRepositorio

class InscripcionControler():
    def __int__(self):
        print("Creando el controlador de Inscripciones")
        self.inscripcionRepositorio = InscripcionRepositorio()
        self.repoEstudiante = EstudianteRepositorio()
        self.repoMateria = MateriaRepositorio()

    'Listado'
    def index(self):
        print("Listado de todos las Inscripciones")
        return self.inscripcionRepositorio.findAll()

    'Creacion'
    def create(self, dataInscripcion, id_estudiante, id_materia):
        inscripcion = Inscripcion(dataInscripcion)
        estudiante = Estudiante(self.repoEstudiante.findById(id_estudiante))
        materia = Materia(self.repoMateria.findById(id_materia))
        inscripcion.estudiante = estudiante
        inscripcion.materia = materia
        return self.repoInscripcion.save(inscripcion)

    'Borrado'
    def delete(self, id):
        print("Borrando la Inscripcion: ", id)
        return self.inscripcionRepositorio.delete(id)

    'Actualizacion'
    def update(self, id, inscripcion):
        print("Actualizando la inscripcion: ", id)
        insActual = (self.inscripcionRepositorio.findById(id))
        insActual.año = inscripcion["año"]
        insActual.semestre = inscripcion["semestre"]
        insActual.NotaFinal = inscripcion["NotaFinal"]
        estudiante = Estudiante(self.repoEstudiante.findById(id_estudiante))
        materia = Materia(self.repoMateria.findById(id_materia))
        inscripcion.estudiante = estudiante
        inscripcion.materia = Materia
        return self.inscripcionRepositorio.save(insActual)

    'Consulta'
    def show(self, id):
        print("Consultando la inscripcion: ", id)
        inscripcion = Inscripcion(self.inscripcionRepositorio.findById(id))
        return inscripcion.__dict__



    def consultarInscritosPorMateria(self, id_materia):
        print("Consultando Inscritos a materia")
        return self.repoInscripcion.getInscripciosMateria(id_materia)

    def consultarNotaPromedio(self, id_materia):
        print("Consultando la nota promedio de la materia")
        return self.repoInscripcion.getNotaPromedio(id_materia)

    def consultarSumatoriaNotas(self, id_materia):
        print("Consultando la Suma de las nota de la materia")
        return self.repoInscripcion.getSumatoriaNotas(id_materia)


