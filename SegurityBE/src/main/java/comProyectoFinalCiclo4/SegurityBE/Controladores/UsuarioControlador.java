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
@RequestMapping("/usuarios")
public class UsuarioControlador {

    //Inyeccion de dependencias
    @Autowired
    private UsuarioRepositorio repositorio;
    @Autowired
    private RolRepositorio rolRepositorio;


    @GetMapping("")
    public List<Usuario> index() {
        return this.repositorio.findAll();
    }

    @PostMapping
    public Usuario create(@RequestBody Usuario dataUsuario){
        dataUsuario.setClave(convertirSHA256(dataUsuario.getClave())); //que es convertirSHA256
        return this.repositorio.save(dataUsuario);
    }

    @PutMapping("{id}")
    public Usuario update(@PathVariable String id, @Requestbody Usuario dataUsuario){
        Usuario usuario = this.repositorio.findById(id).orElse(null);
        if(usuario != null){
            usuario.setSeudonimo((dataUsuario.getSeudonimo()));
            usuario.setCorreo(dataUsuario.getCorreo());
            usuario.setClave(convertirSHA256(dataUsuario.getClave()));
            return this.repositorio.save(usuario);
        } else {
            return null;
        }
    }

    @GetMapping("{id}")
    public Usuario show(@PathVariable String id){
        Usuario us = this.repositorio.findById(id).orElse(null);
        return us;
    }

    @ResponseStatus(HttpStatus.NO_CONTENT)
    @DeleteMapping("{id}")
    public void delete(@PathVariable String id){
        Usuario us = this.repositorio.findById(id).orElse(null);
        if (us != null) {
            this.repositorio.delete(us);
        }
    }

    //Asignar Rol
    @PutMapping("{id}/rol/{id_rol}")
    public Usuario asignarRolAUsuario(@PathVariable String id, @PathVariable String id_rol){
        Usuario usr = this.repositorio.findById(id).orElse(null);
        Rol rol = this.rolRepositorio.findById(id).orElse(null);

        if(usr != null && rol != null){
            usr.setRol(rol);
            return this.repositorio.save(usr);
        } else {
            return null;
        }
    }


    //cifrado de clave
    private String convertirSHA256(String clave){
        //libreria propia para manejo y cifrados
        MessageDigest ms = null;
        try {
            md = MessageDigest.getInstance("SHA-256");
        } catch (NoSuchAlgorithmException ex) {
            ex.printStackTrace();
            return null;
        }
        byte[] hash = md.digest(clave.getBytes());
        StringBuffer sb = new StringBuffer();
        for(byte b : hash) {
            sb.append(String.format("%02x", b));
        }
        return sb.toString();
    }
}
