# Patrón Factory Method

<aside>
💡 El patrón Factory Method es un patrón de diseño creacional que proporciona una interfaz para crear objetos en una superclase, pero permite a las subclases decidir qué clase concreta instanciar. 

Esto permite que una clase delegue la creación de objetos a sus subclases.

</aside>

<br>

### Ejemplo básico de Patrón

- En un ORM de algún framework como Laravel se escribe únicamente en el archivo de configuración el nombre de la base de datos y las credenciales, lo que hacen internamente es:
    1. recibir el tipo de base de datos que se usa (pe: MySQL, PostgreSQL, etc.)
    2. Mediante una fabrica consultan el controlador correcto y utilizan las credenciales para hacer la conexión con el controlador correcto y las credenciales correctas

<br>

### Aplicabilidad

El patrón Factory Method es adecuado cuando:

- Se necesita una flexibilidad en la creación de objetos y se desea que la decisión de qué objeto concreto crear sea tomada por las subclases.
- Se desea evitar acoplar el código cliente a clases concretas, permitiendo así la extensibilidad del sistema.
- Se desea proporcionar una interfaz común para crear objetos, pero permitiendo que las subclases decidan la implementación concreta.

<br>

### Estructura

El patrón Factory Method generalmente se compone de los siguientes elementos:

- **Producto**: Define la interfaz común para los objetos que el Factory Method crea.
- **Producto Concreto**: Son las implementaciones concretas del Producto.
- **Creador**: Define el Factory Method que devuelve un objeto del tipo Producto.
- **Creador Concreto**: Implementa el Factory Method y devuelve una instancia específica de Producto.

<br>

### Notas importantes

- El patrón Factory Method permite a las subclases decidir qué clase concreta instanciar, brindando así una mayor flexibilidad y extensibilidad.
- El patrón Factory Method se centra en la creación de objetos, dejando la lógica específica de cada objeto a las subclases.
- El patrón Factory Method puede combinarse con otros patrones, como el patrón Template Method, para proporcionar una estructura más flexible y modular.

<br>

### Conclusiones

El patrón Factory Method proporciona una forma elegante de abstraer la creación de objetos, permitiendo que las subclases tomen decisiones sobre qué objetos concretos crear. Esto promueve la flexibilidad y extensibilidad del sistema, ya que el código cliente no está acoplado a las clases concretas. El patrón Factory Method es ampliamente utilizado en muchas aplicaciones, especialmente cuando se trabaja con jerarquías de clases y se necesita delegar la responsabilidad de creación a las subclases.