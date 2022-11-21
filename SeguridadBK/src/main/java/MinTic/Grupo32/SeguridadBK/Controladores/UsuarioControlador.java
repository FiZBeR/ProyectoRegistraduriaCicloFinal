package MinTic.Grupo32.SeguridadBK.Controladores;


import MinTic.Grupo32.SeguridadBK.Modelos.Usuario;
import MinTic.Grupo32.SeguridadBK.Modelos.Rol;
import MinTic.Grupo32.SeguridadBK.Repositorios.PermisosRolRepositorio;
import MinTic.Grupo32.SeguridadBK.Repositorios.RolRepositorio;
import MinTic.Grupo32.SeguridadBK.Repositorios.UsuarioRepositorio;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;/*Para que sirve*/
import org.springframework.http.HttpStatus;/*Para que sirve*/
import org.springframework.web.bind.annotation.*;/*Para que sirve*/

import javax.servlet.http.HttpServletResponse;/*Para que sirve*/
import java.io.IOException;/*Para que sirve*/
import java.security.MessageDigest;/*Para que sirve*/
import java.security.NoSuchAlgorithmException;/*Para que sirve*/
import java.util.List;


@CrossOrigin //Que son las referencias cruzadas
@RestController
//@RequestMapping("/usuarios")/*Aca estamos definiendo una ruta principal para los demas servicios con eso no las tenemos que volver a declarar si no para darle una extencion como es en el caso de la linea 46*/
public class UsuarioControlador {

    //Inyeccion de dependencias
    @Autowired
    private UsuarioRepositorio repositorio;
    @Autowired
    private RolRepositorio rolRepositorio;
/*Microservicios de usuarios------------------------------------------------------------------------------------*/
    /*Obtener todo*/
    @GetMapping("/usuarios")
    public List<Usuario> index() {

        return this.repositorio.findAll();
    }
/*Crear*/
    @PostMapping("/usuarios")
    public Usuario create(@RequestBody Usuario dataUsuario){ /*para poder utilizar los datos que vienen en la anotacion usamos requetbody*/
        dataUsuario.setClave(convertirSHA256(dataUsuario.getClave())); //que es convertirSHA256
        return this.repositorio.save(dataUsuario);
    }

    @PutMapping("/usuarios/{id}")
    public Usuario update(@PathVariable String id, @RequestBody Usuario dataUsuario){
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

    @GetMapping("/usuarios/{id}")
    public Usuario show(@PathVariable String id){
        Usuario us = this.repositorio.findById(id).orElse(null);
        return us;
    }

    @ResponseStatus(HttpStatus.NO_CONTENT)/*Para lo quenos ayuda esta anotacion es para qu a nivel del cliente se responda que no se hayo contenido respecto al string solicitado*/
    @DeleteMapping("/usuarios/{id}")
    public void delete(@PathVariable String id){
        Usuario us = this.repositorio.findById(id).orElse(null);
        if (us != null) {
            this.repositorio.delete(us);
        }
    }
/**/
    //Asignar Rol
    @PutMapping("{id}/rol/{id_rol}")
    public Usuario asignarRolAUsuario(@PathVariable String id, @PathVariable String id_rol){
        Usuario usr = this.repositorio.findById(id).orElse(null);/*Consultamos el usuario*/
        Rol rol = this.rolRepositorio.findById(id).orElse(null);/**/

        if(usr != null && rol != null){
            usr.setRol(rol);
            return this.repositorio.save(usr);
        } else {
            return null;
        }
    }

    
    /*Verificacion de Credenciales por ApiGateway*/
    @PostMapping("/validar")
    public Usuario validar(@RequestBody Usuario usuario, final HttpServletResponse rta) throws IOException {
        Usuario usr = this.repositorio.getUsuarioPorCorreo(usuario.getCorreo());
        String clave = convertirSHA256(usuario.getClave());

        if(usr != null && clave.equals(usr.getClave())) {
            usr.setClave("");
            return  usr;
        } else {
            rta.sendError(HttpServletResponse.SC_UNAUTHORIZED);/*Para que sirve esta linea*/
            return null;
        }
    }


    //cifrado de clave
    private String convertirSHA256(String clave){
        //libreria propia para manejo y cifrados
        MessageDigest md = null;
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

/*
* Creamos un metodo string que se llama convertirSHA256 que resive un string clave, usamos una libreria exclusiva
* para el manejo de cifrados MessageDigestm, le creamos una variable y despues un try donde tengamos una excepcion
* controlada
* */
