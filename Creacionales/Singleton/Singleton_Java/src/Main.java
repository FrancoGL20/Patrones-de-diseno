public class Main {
    public static void main(String[] args) {

        // Sin el patron Singleton
        System.out.println("Sin el patron Singleton");
        MyObject a=new MyObject("a");
        MyObject b=new MyObject("b");

        System.out.println(a.getX());
        System.out.println(b.getX());


        // Con el patron Singleton
        System.out.println("\nCon el patron Singleton");
        MySingleton c=MySingleton.getMySingleton("c");
        MySingleton d=MySingleton.getMySingleton("d");

        System.out.println(c.getX());
        System.out.println(d.getX());
    }
}

/* Salida:

Sin el patron Singleton
a
b

Con el patron Singleton
Ya existe una instancia de MySingleton
d
d

*/