package comProyectoFinalCiclo4.SegurityBE.Repositorios;

import comProyectoFinalCiclo4.SegurityBE.Modelos.Usuario;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface UsuarioRepositorio extends MongoRepository<Usuario, String> {
}
