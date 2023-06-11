import java.sql.Connection;

// PRODUCTO CONCRETO
public class OracleAdapter implements DBAdapter {
    @Override
    public Connection getConnection() {
        Connection connection = null;
        return connection;
    }
}
