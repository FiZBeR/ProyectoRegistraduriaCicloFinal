package comProyectoFinalCiclo4.SegurityBE.Controladores;

import comProyectoFinalCiclo4.SegurityBE.Modelos.PermisosRol;
import comProyectoFinalCiclo4.SegurityBE.Modelos.Permiso;
import comProyectoFinalCiclo4.SegurityBE.Modelos.Rol;
import comProyectoFinalCiclo4.SegurityBE.Repositorios.PermisoRepositorio;
import comProyectoFinalCiclo4.SegurityBE.Repositorios.PermisosRolRepositorio;
import comProyectoFinalCiclo4.SegurityBE.Repositorios.RolRepositorio;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

public class PermisosRolControlador {

    private PermisosRolRepositorio repositorioPermisosRol;
    @Autowired
    private PermisoRepositorio repositorioPermisos;
    private RolRepositorio repositorioRol;

    @PostMapping("rol/{id_rol}/permiso/{id_permiso}")
    public PermisosRol create(@PathVariable String id_rol, @PathVariable String id_permiso){
        Permiso p = this.repositorioPermisos.finById(id_permiso).orElse(null);
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


    @PutMapping("{id}/rol/{id_rol}/permiso/{id_permiso}")
    public PermisosRol update(@PathVariable String id, @PathVariable String id_rol, @PathVariable String id_permiso){
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
    /*
    Los microservicios de listado, consulta, borrado etc se implementan de manera similar al de usuario
     */


    @GetMapping("validar-permiso/rol/{id_rol}")
    public PermisosRol getPermiso(@PathVariable String id_rol, @RequestBody Permiso dataPermiso){
        Rol r = this.repositorioRol.findById(id_rol);
        Permiso p = this.repositorioPermisos.getPermiso(dataPermiso.getUrl(), dataPermiso.getMetodo());

        if(r != null && p != null){
            return this.repositorioPermisosRol.getPermisosRol(r.getId(), p.getId());
        } else {
            return  null;
        }
    }


}
