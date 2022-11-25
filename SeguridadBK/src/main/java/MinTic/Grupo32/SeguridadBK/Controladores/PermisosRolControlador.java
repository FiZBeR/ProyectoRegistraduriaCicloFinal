package MinTic.Grupo32.SeguridadBK.Controladores;

import MinTic.Grupo32.SeguridadBK.Modelos.PermisosRol;
import MinTic.Grupo32.SeguridadBK.Modelos.Permiso;
import MinTic.Grupo32.SeguridadBK.Modelos.Rol;
import MinTic.Grupo32.SeguridadBK.Repositorios.PermisoRepositorio;
import MinTic.Grupo32.SeguridadBK.Repositorios.PermisosRolRepositorio;
import MinTic.Grupo32.SeguridadBK.Repositorios.RolRepositorio;
import org.springframework.beans.AbstractNestablePropertyAccessor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@CrossOrigin //Que son las referencias cruzadas
@RestController
//@RequestMapping("/roles")
public class PermisosRolControlador {
    @Autowired
    private PermisosRolRepositorio repositorioPermisosRol;
    @Autowired
    private PermisoRepositorio repositorioPermisos;
    @Autowired
    private RolRepositorio repositorioRol;


    //Crear
    @PostMapping("/rol/{id_rol}/permiso/{id_permiso}")
    public PermisosRol create(@PathVariable String id_rol, @PathVariable String id_permiso){
        Permiso p = this.repositorioPermisos.findById(id_permiso).orElse(null);
        Rol r = this.repositorioRol.findById(id_rol).orElse(null);
        if(p != null && r != null) {
            PermisosRol pr = new PermisosRol();
            pr.setPermiso(p);
            pr.setRol(r);
            return this.repositorioPermisosRol.save(pr);
        } else {
            return null;
        }
    }


    @PutMapping("/{id}/rol/{id_rol}/permiso/{id_permiso}")
    public PermisosRol update(@PathVariable String id,
                              @PathVariable String id_rol,
                              @PathVariable String id_permiso){
        Rol r = this.repositorioRol.findById(id_rol).orElse(null);
        Permiso p = this.repositorioPermisos.findById(id_permiso).orElse(null);
        PermisosRol pr = this.repositorioPermisosRol.findById(id).orElse(null);
        if(r != null && p != null && pr != null) {
            pr.setRol(r);
            pr.setPermiso(p);
            return this.repositorioPermisosRol.save(pr);
        } else {
            return null;
        }
    }

    @GetMapping("/permisosrol")
    public List<PermisosRol> index() {

        return this.repositorioPermisosRol.findAll();
    }

    @GetMapping("/permisosrol/{id}")
    public PermisosRol show(@PathVariable String id){
        PermisosRol us = this.repositorioPermisosRol.findById(id).orElse(null);
        return us;
    }

    @ResponseStatus(HttpStatus.NO_CONTENT)/*Para lo quenos ayuda esta anotacion es para qu a nivel del cliente se responda que no se hayo contenido respecto al string solicitado*/
    @DeleteMapping("/permisosrol/{id}")
    public void delete(@PathVariable String id){
        PermisosRol pr = this.repositorioPermisosRol.findById(id).orElse(null);
        if (pr != null) {
            this.repositorioPermisosRol.delete(pr);
        }
    }

   /*@GetMapping("valida-permiso/rol/{id_rol}")
    public PermisosRol getPermiso(@PathVariable String id_rol, @RequestBody Permiso dataPermiso){
        Rol r = this.repositorioRol.findById(id_rol);
        Permiso p = this.repositorioPermisos.getPermiso(dataPermiso.getUrl(), dataPermiso.getMetodo());

        if(r != null && p != null){
            return this.repositorioPermisosRol.getPermisosRol(r.getId(), p.getId());
        } else {
            return  null;
        }
    }*/
}
