package comProyectoFinalCiclo4.SegurityBE.Repositorios;

import comProyectoFinalCiclo4.SegurityBE.Modelos.Permiso;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;

public interface PermisoRepositorio extends MongoRepository<Permiso, String> {
    @Query("{'url':?0, 'metodo':?1}")
    Permiso getPermiso(String url, String metodo);

}
