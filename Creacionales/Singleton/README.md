# Patrón Singleton

<aside>
💡 Su objetivo es garantizar que una clase tenga una única instancia y proporcionar un punto global de acceso a ella.

</aside>

<br>

## Aplicabilidad

El patrón Singleton es adecuado cuando:

- Se requiere tener una única instancia de una clase en todo el sistema.
- Dicha instancia única necesita ser accesible de forma global en diferentes partes del código.
- Es necesario controlar el acceso concurrente a la instancia única.

<br>

## Estructura

El patrón Singleton generalmente se compone de los siguientes elementos:

- **Singleton**: Es la clase que implementa el patrón. Tiene una variable estática privada que almacena la instancia única y un método estático para acceder a ella. La clase Singleton controla la creación de la instancia única y garantiza que solo haya una instancia en todo momento.

<br>

## Notas importantes

- La implementación del Singleton debe tener en cuenta la concurrencia. Si múltiples hilos intentan acceder al Singleton al mismo tiempo, puede ocurrir una condición de carrera. Para abordar este problema, se pueden aplicar técnicas como la sincronización o el uso de inicialización perezosa con doble bloqueo.
- Es importante tener en cuenta que el patrón Singleton puede introducir acoplamiento en el código y dificultar las pruebas unitarias. Por lo tanto, se recomienda utilizarlo cuando realmente sea necesario y se justifique su uso.