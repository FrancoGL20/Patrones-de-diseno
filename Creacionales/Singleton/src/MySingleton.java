public class MySingleton {
    String x;

    private static MySingleton mySingleton = null;

    private MySingleton(String x) {
        this.x = x;
    }

    public static MySingleton getMySingleton(String x) {
        if (mySingleton == null) {
            mySingleton = new MySingleton(x);
        }else{
            System.out.println("Ya existe una instancia de MySingleton");
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
