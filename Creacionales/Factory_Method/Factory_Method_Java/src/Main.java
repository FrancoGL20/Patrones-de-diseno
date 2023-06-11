import java.sql.Connection;
import java.sql.SQLException;
import java.sql.Statement;

public class Main {
    public static void main(String[] args) throws SQLException {
        // Se crea un producto concreto gracias al creador y creador concreto (DBFactory)
        DBAdapter dbAdapter = DBFactory.getAdapter(DBFactory.DBType.MySQL);

        // Se utiliza el producto concreto ...
        Connection connection = dbAdapter.getConnection();
        Statement statement = connection.createStatement();
        statement.execute("SELECT * FROM XXXX");
    }
}
