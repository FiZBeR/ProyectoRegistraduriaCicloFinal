package MinTic.Grupo32.SeguridadBK.Repositorios;

import MinTic.Grupo32.SeguridadBK.Modelos.Usuario;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;/**/

public interface UsuarioRepositorio extends MongoRepository<Usuario, String> {

    @Query("{'correo': ?0}")/*Aca decimos que a nuestra entidad usuario le pedimos el correo y que este objeto sea el primero del parametro*/
    public Usuario getUsuarioPorCorreo(String correo);

}
