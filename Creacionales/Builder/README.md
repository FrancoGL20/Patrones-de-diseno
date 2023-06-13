# Patrón Builder

<aside>
💡 El patrón Builder es un patrón de diseño creacional que permite construir objetos complejos paso a paso.

Separando la construcción de un objeto de su representación, el patrón Builder permite que el mismo proceso de construcción pueda crear diferentes representaciones.

</aside>

<br>

### Aplicabilidad

El patrón Builder es adecuado cuando:

- Se necesita construir objetos complejos que requieren una secuencia específica de pasos.
- Se desea crear diferentes representaciones de un objeto utilizando el mismo proceso de construcción.
- Se quiere desacoplar la construcción de un objeto de su representación, permitiendo diferentes implementaciones de la construcción.

<br>

### Estructura

El patrón Builder generalmente se compone de los siguientes elementos:

- **Builder (Constructor)**: Define una interfaz para construir diferentes partes de un producto. Proporciona métodos para construir cada parte del producto y un método para obtener el resultado final.
    - **Concrete Builder (Constructor concreto)**: Implementa la interfaz Builder y proporciona implementaciones específicas para construir diferentes partes del producto. Mantiene un estado interno para almacenar el producto en construcción.
- **Product (Producto)**: Representa el objeto complejo que se está construyendo.
    
    El Builder construye el producto utilizando los métodos proporcionados por el Concrete Builder.
    
- **Client (Cliente)**: Es el código que utiliza tanto al Director como al Concrete builder para construir el producto. El cliente configura el Director con un Builder concreto y luego inicia el proceso de construcción llamando al método de construcción en el Director.
    - **Director**: Es responsable de utilizar el objeto **Builder** para construir el producto final.
        
        Conoce la metodología (pasos) de construcción del Concrete builder que le es enviado por el Cliente y lo crea.

<br>

### Conclusiones

El patrón Builder permite construir objetos complejos paso a paso, separando la construcción de un objeto de su representación final. Esto proporciona flexibilidad en el proceso de construcción y permite crear diferentes representaciones del mismo objeto. El patrón Builder es útil cuando se necesita construir objetos complejos con una secuencia específica de pasos y se desea desacoplar la construcción del objeto de su representación.