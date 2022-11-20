package MinTic.Grupo32.SeguridadBK.Controladores;


import MinTic.Grupo32.SeguridadBK.Modelos.Permiso;
import MinTic.Grupo32.SeguridadBK.Repositorios.PermisoRepositorio;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@CrossOrigin //Que son las referencias cruzadas
@RestController
@RequestMapping("/Permiso")

public class PermisoControlador {

    @Autowired
    private PermisoRepositorio permisosRepositorio;

    /*Obtener todo*/
    @GetMapping("")
    public List<Permiso> index() {
        return this.permisosRepositorio.findAll();
    }
    /*Crear*/
    @PostMapping("")
    public Permiso create(@RequestBody Permiso dataPermiso){ /*para poder utilizar los datos que vienen en la anotacion usamos requetbody*/
        return this.permisosRepositorio.save(dataPermiso);
    }
    /*actualizar*/
    @PutMapping("{id}")
    public Permiso update(@PathVariable String id, @RequestBody Permiso dataPermiso){
        Permiso pr = this.permisosRepositorio.findById(id).orElse(null);
        if(pr != null){
            pr.setId((dataPermiso.getId()));
            pr.setMetodo(dataPermiso.getMetodo());
            pr.setUrl(dataPermiso.getUrl());
            return this.permisosRepositorio.save(pr);
        } else {
            return null;
        }
    }
    /*Buscar por id*/
    @GetMapping("{id}")
    public Permiso show(@PathVariable String id){
        Permiso rol = this.permisosRepositorio.findById(id).orElse(null);
        return rol;
    }
    /*Borrar*/
    @ResponseStatus(HttpStatus.NO_CONTENT)/*Para lo quenos ayuda esta anotacion es para qu a nivel del cliente se responda que no se hayo contenido respecto al string solicitado*/
    @DeleteMapping("{id}")
    public void delete(@PathVariable String id){
        Permiso rl = this.permisosRepositorio.findById(id).orElse(null);
        if (rl != null) {
            this.permisosRepositorio.delete(rl);
        }
    }
}
