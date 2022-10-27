from Modelos.Departamento import Departamento
from Repositorio.DepartamentoRepositorio import DepartamentoRepositorio

class DepartamentoControler():
    def __int__(self):
        print("Construyendo Controlador de Departamento")
        self.departamentoRepositorio = DepartamentoRepositorio()


    'Listado'
    def index(self):
        print("Listado de todos los Departamento")
        return self.departamentoRepositorio.findAll()

    'Creacion'
    def create(self, unDepartamento):
        print("Creando el Departamento")
        departamento = Departamento(unDepartamento)
        return self.departamentoRepositorio.save(unDepartamento)


    'Borrado'
    def delete(self, id):
        print("Borrando Departamento: ", id)
        return self.departamentoRepositorio.delete(id)

    'Actualizacion'
    def update(self, id, departamento):
        print("Actualizando rl Departamento: ", id)
        depActual = (self.departamentoRepositorio.findById(id))
        depActual.cedula = departamento["cedula"]
        depActual.nombre = departamento["nombre"]
        depActual.apellido = departamento["apellido"]
        return self.departamentoRepositorio.save(depActual)

    'Consulta'
    def show(self, id):
        print("Consultando el departamento: ", id)
        departamento = Departamento(self.departamentoRepositorio.findById(id))
        return departamento.__dict__