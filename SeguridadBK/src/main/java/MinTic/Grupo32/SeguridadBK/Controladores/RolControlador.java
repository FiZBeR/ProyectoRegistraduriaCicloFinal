package MinTic.Grupo32.SeguridadBK.Controladores;

import MinTic.Grupo32.SeguridadBK.Modelos.Rol;
import MinTic.Grupo32.SeguridadBK.Repositorios.RolRepositorio;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;/*Para que sirve*/
import org.springframework.http.HttpStatus;/*Para que sirve*/
import org.springframework.web.bind.annotation.*;/*Para que sirve*/


import java.util.List;


@CrossOrigin //Que son las referencias cruzadas
@RestController
@RequestMapping("/roles")
public class RolControlador {

    /*@Autowired
    private UsuarioRepositorio repositorio;*/
    @Autowired
    private RolRepositorio rolRepositorio;


    /*Obtener todo*/
    @GetMapping("")
    public List<Rol> index() {
        return this.rolRepositorio.findAll();
    }
    /*Crear*/
    @PostMapping("")
    public Rol create(@RequestBody Rol dataRol){ /*para poder utilizar los datos que vienen en la anotacion usamos requetbody*/
        return this.rolRepositorio.save(dataRol);
    }
    /*actualizar*/
    @PutMapping("{id}")
    public Rol update(@PathVariable String id, @RequestBody Rol dataRol){
        Rol rol = this.rolRepositorio.findById(id).orElse(null);
        if(rol != null){
            rol.setId((dataRol.getId()));
            rol.setNombre(dataRol.getNombre());
            return this.rolRepositorio.save(rol);
        } else {
            return null;
        }
    }
    /*Buscar por id*/
    @GetMapping("{id}")
    public Rol show(@PathVariable String id){
        Rol rol = this.rolRepositorio.findById(id).orElse(null);
        return rol;
    }
    /*Borrar*/
    @ResponseStatus(HttpStatus.NO_CONTENT)/*Para lo quenos ayuda esta anotacion es para qu a nivel del cliente se responda que no se hayo contenido respecto al string solicitado*/
    @DeleteMapping("{id}")
    public void delete(@PathVariable String id){
        Rol rl = this.rolRepositorio.findById(id).orElse(null);
        if (rl != null) {
            this.rolRepositorio.delete(rl);
        }
    }
}
