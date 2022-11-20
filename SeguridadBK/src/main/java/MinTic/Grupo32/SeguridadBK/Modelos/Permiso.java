package MinTic.Grupo32.SeguridadBK.Modelos;
import org.springframework.data.mongodb.core.mapping.Document;

@Document()
public class Permiso {
    private String id;
    private String url;
    private String metodo;


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    public String getMetodo() {
        return metodo;
    }

    public void setMetodo(String metodo) {
        this.metodo = metodo;
    }
}
