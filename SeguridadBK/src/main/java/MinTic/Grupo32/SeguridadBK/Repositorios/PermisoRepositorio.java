package MinTic.Grupo32.SeguridadBK.Repositorios;

import MinTic.Grupo32.SeguridadBK.Modelos.Permiso;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;

import java.util.Optional;

public interface PermisoRepositorio extends MongoRepository<Permiso, String> {
    @Query("{'url':?0, 'metodo':?1}")
    Permiso getPermiso(String url, String metodo);

}
