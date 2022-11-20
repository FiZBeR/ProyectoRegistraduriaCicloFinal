package MinTic.Grupo32.SeguridadBK.Repositorios;

import MinTic.Grupo32.SeguridadBK.Modelos.Rol;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface RolRepositorio extends MongoRepository<Rol, String>{
}