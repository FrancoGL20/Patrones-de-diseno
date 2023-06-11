public class DBFactory {

    // CREADOR
    public enum DBType {
        MySQL, Oracle, PostgreSQL
    }
    
    // CREADOR CONCRETO
    public static DBAdapter getAdapter(DBType dbType) {
        switch (dbType) {
            case MySQL:
                return new MySQLAdapter();
            case Oracle:
                return new OracleAdapter();
            case PostgreSQL:
                return new PostgreSQLAdapter();
            default:
                throw new IllegalArgumentException("Tipo de base de datos no soportada");
        }
    }

}
