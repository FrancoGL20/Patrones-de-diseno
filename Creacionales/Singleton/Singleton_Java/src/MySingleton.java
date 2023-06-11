public class MySingleton {
    // Atributo cualquiera
    private String x;

    // Instancia unica
    private static MySingleton mySingleton = null;

    // Constructor privado
    private MySingleton(String x) {
        this.x = x;
    }

    public static MySingleton getMySingleton(String x) {
        if (mySingleton == null) {
            mySingleton = new MySingleton(x);
        }else{
            System.out.println("Ya existe una instancia de MySingleton");
            mySingleton.setX(x);
        }
        return mySingleton;
    }

    public String getX() {
        return this.x;
    }

    public void setX(String x) {
        this.x = x;
    }
}
