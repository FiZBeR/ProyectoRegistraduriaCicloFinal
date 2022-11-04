package comProyectoFinalCiclo4.SegurityBE.Controladores;

import comProyectoFinalCiclo4.SegurityBE.Modelos.Usuario;
import comProyectoFinalCiclo4.SegurityBE.Modelos.Rol;
import comProyectoFinalCiclo4.SegurityBE.Repositorios.PermisosRolRepositorio;
import comProyectoFinalCiclo4.SegurityBE.Repositorios.RolRepositorio;
import comProyectoFinalCiclo4.SegurityBE.Repositorios.UsuarioRepositorio;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.List;

@CrossOrigin //Que son las referencias cruzadas
@RestController
@RequestMapping("/Permiso")

public class PermisoControlador {
}
