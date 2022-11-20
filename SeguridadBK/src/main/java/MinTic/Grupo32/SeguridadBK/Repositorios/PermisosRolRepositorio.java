package MinTic.Grupo32.SeguridadBK.Repositorios;

import MinTic.Grupo32.SeguridadBK.Modelos.PermisosRol;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;

public interface PermisosRolRepositorio extends MongoRepository<PermisosRol, String> {

    @Query("{'rol.$id': ObjectId(?0), 'permiso.$id': ObjectId(?1) }")
    public PermisosRol getPermisosRol(String id_rol, String id_permiso);

}