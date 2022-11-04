package comProyectoFinalCiclo4.SegurityBE.Repositorios;

import comProyectoFinalCiclo4.SegurityBE.Modelos.PermisosRol;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface PermisosRolRepositorio extends MongoRepository<PermisosRol, String> {
}
