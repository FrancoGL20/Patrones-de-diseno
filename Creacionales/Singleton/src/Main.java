public class Main {
    public static void main(String[] args) {
        MySingleton a=MySingleton.getMySingleton("a");
        MySingleton b=MySingleton.getMySingleton("b");

        System.out.println(a.getX());
        System.out.println(b.getX());
    }
}