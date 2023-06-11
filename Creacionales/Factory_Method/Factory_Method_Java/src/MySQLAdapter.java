import java.sql.Connection;

// PRODUCTO CONCRETO
public class MySQLAdapter implements DBAdapter {
    @Override
    public Connection getConnection() {
        Connection connection = null;
        return connection;
    }
}
