package comProyectoFinalCiclo4.SegurityBE.Repositorios;

import comProyectoFinalCiclo4.SegurityBE.Modelos.Permiso;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface PermisoRepositorio extends MongoRepository<Permiso, String> {
}
