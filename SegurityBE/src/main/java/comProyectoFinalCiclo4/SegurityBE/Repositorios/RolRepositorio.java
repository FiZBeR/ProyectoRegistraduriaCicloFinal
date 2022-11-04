package comProyectoFinalCiclo4.SegurityBE.Repositorios;

import comProyectoFinalCiclo4.SegurityBE.Modelos.Rol;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface RolRepositorio extends MongoRepository<Rol, String> {
}
