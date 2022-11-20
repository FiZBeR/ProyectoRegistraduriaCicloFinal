package MinTic.Grupo32.SeguridadBK.Modelos;
import org.springframework.data.mongodb.core.mapping.Document;

/*
Completar las anotaciones para los modelos
 */
@Document()
public class PermisosRol {
    /*private String id;
    private String id_rol;
    private String id_permiso;*/

    public Permiso getPermiso() {
        return permiso;
    }

    public void setPermiso(Permiso permiso) {
        this.permiso = permiso;
    }

    public Rol getRol() {
        return rol;
    }

    public void setRol(Rol rol) {
        this.rol = rol;
    }

    private Permiso permiso;

    private Rol rol;

    /*public PermisosRol(String id, String id_rol, String id_permiso) {
        this.id = id;
        this.id_rol = id_rol;
        this.id_permiso = id_permiso;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getId_rol() {
        return id_rol;
    }

    public void setId_rol(String id_rol) {
        this.id_rol = id_rol;
    }

    public String getId_permiso() {
        return id_permiso;
    }

    public void setId_permiso(String id_permiso) {
        this.id_permiso = id_permiso;
    }*/
}
