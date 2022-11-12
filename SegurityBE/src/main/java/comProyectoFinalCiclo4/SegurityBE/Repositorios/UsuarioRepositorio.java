package comProyectoFinalCiclo4.SegurityBE.Repositorios;

import comProyectoFinalCiclo4.SegurityBE.Modelos.Usuario;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;

public interface UsuarioRepositorio extends MongoRepository<Usuario, String> {

    @Query("{'correo': ?0}")
    public Usuario getUsuarioPorCorreo(String correo):

}
