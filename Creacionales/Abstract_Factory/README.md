<aside>
💡 Su objetivo principal es proporcionar una interfaz para crear familias de objetos relacionados o dependientes sin especificar sus clases concretas. 

Permite la creación de objetos relacionados pero independientes de las clases concretas utilizadas.

*”Permite fabricar fábricas” ó es “Es una fábrica de fábricas”*

</aside>

<br>

### Aplicabilidad

El patrón Abstract Factory es adecuado cuando:

- Se desea crear objetos que estén relacionados o dependan entre sí.
- Se desea ocultar la creación de objetos y proporcionar una interfaz común para crear diferentes tipos de objetos.
- Se necesita que el código cliente sea independiente de las clases concretas utilizadas para crear objetos.

<br>

### Estructura

El patrón Abstract Factory generalmente se compone de los siguientes elementos:

- **Abstract Factory (Fábrica abstracta)**: Es una interfaz o clase abstracta que declara métodos para la creación de objetos de una familia de productos.
- **Concrete Factory (Fábrica concreta)**: Son las implementaciones concretas de la interfaz Abstract Factory. Cada Concrete Factory es responsable de crear una familia específica de productos.
- **Abstract Product (Producto abstracto, Producto)**: Es una interfaz o clase abstracta que declara la interfaz común para los productos de una familia.
    - **Specific Product (Inventado, NO OFICIAL)**: clases más especificas, aún interfaces, pero que son implementadas en el ******Concrete Product******
- **Concrete Product (Producto concreto)**: Son las implementaciones concretas de la interfaz Abstract Product. Cada Concrete Product es una variante específica de un producto dentro de una familia.
- **Client**: Es el código que utiliza la interfaz [Abstract Factory](https://www.notion.so/Patrones-de-dise-o-de-software-552147a56fdb4b4cb483d6b5621bf6cb?pvs=21) para crear objetos de la familia de productos. El cliente interactúa con los productos a través de sus interfaces abstractas.

<br>

### Notas importantes

- El patrón Abstract Factory permite crear objetos relacionados y dependientes sin acoplar el código cliente a clases concretas.
- Se pueden tener múltiples familias de productos y varias implementaciones de las Abstract Factories para crear cada familia.
- El patrón Abstract Factory promueve la coherencia entre los productos de una familia y garantiza que solo se utilicen productos compatibles entre sí.

<br>

### Conclusiones

El patrón Abstract Factory proporciona una forma estructurada de crear familias de objetos relacionados. 

Permite la creación de objetos independientes de las clases concretas utilizadas y proporciona una interfaz común para interactuar con los productos. 

El patrón Abstract Factory es útil cuando se necesita gestionar múltiples familias de productos y se desea mantener un código cliente flexible y extensible.