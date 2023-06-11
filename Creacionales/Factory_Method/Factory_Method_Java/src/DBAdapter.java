import java.sql.Connection;

// PRODUCTO
public interface DBAdapter {
    // Método que debe ser implementado por los productos concretos
    Connection getConnection();
}