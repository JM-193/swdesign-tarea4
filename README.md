# swdesign-tarea4

[Enlace al repo](https://github.com/JM-193/swdesign-tarea4)

## Información Personal

* José Manuel Mora Z - C35280
* Diseño de Software - CI-0136
* Escuela de las Ciencias de la Computación e Informática (ECCI)
* Universidad de Costa Rica (UCR)

Sistema de gestión de pedidos para una cafetería que implementa patrones de diseño para manejar personalización de productos, notificaciones y procesamiento de órdenes.

## Descripción del Problema

Una cafetería necesita digitalizar su proceso de pedidos con las siguientes funcionalidades:

* Los clientes pueden ordenar bebidas (café, té, ...) y alimentos (croissants, tostadas, muffins, ...)
* Pueden personalizar sus órdenes con extras (leche, canela, crema, rellenos, toppings, ...)
* El sistema debe manejar pedidos que se preparan, notifican y entregan

## Patrones de Diseño Implementados

### 1. Patrón Decorator

**Razón de uso:** El patrón Decorator es ideal para agregar funcionalidades adicionales a objetos de manera dinámica y flexible. En este caso, lo usamos para personalizar bebidas y alimentos con diferentes extras.

**Implementación:**

* En el archivo `DecoratorPattern.py`
* `MenuItem`: Interfaz base para todos los items del menú
* `Beverage` y `Food`: Componentes concretos base
* `MenuItemDecorator`: Clase decoradora abstracta
* Decoradores concretos: `MilkDecorator`, `CreamDecorator`, `DoubleEspressoDecorator`, `CinnamonDecorator`, `ChocolateFillingDecorator`, `HamCheeseFillingDecorator`, `CaramelToppingDecorator`

**Ventajas:**

* Permite combinar múltiples extras sin crear subclases para cada combinación posible
* Cumple con el principio Open/Closed: abierto a extensión, cerrado a modificación
* Fácil agregar nuevos decoradores sin modificar código existente
* Cada decorador tiene una responsabilidad única (SRP - Single Responsibility Principle)

**Ejemplo de uso:**

```python
cafe = Beverage("Cafe", 2.5)
cafe = MilkDecorator(cafe)
cafe = CinnamonDecorator(cafe)
# Resultado: "Cafe con leche y canela"
```

**Notas Adicionales:**

Se incluye un método `_add_extra()` en la clase `MenuItemDecorator` para facilitar la semántica al agregar extras. El método detecta si ya se ha agregado otros extra y ajusta la descripción en consecuencia, agregando "con", "y" o comas según sea necesario.

Para la clase `DoubleEspressoDecorator`, no se utiliza este método ya que la descripción se agrega antes del nombre del ítem base (está en Inglés), siendo que el método no es abstracto, se permite la flexibilidad de no usarlo en estos casos específicos.

### 2. Patrón Observer

**Razón de uso:** El patrón Observer establece una dependencia uno-a-muchos entre objetos, de manera que cuando un objeto cambia de estado, todos sus dependientes son notificados automáticamente. Perfecto para el sistema de notificaciones de pedidos.

**Implementación:**

* En el archivo `ObserverPattern.py`
* `Observer`: Interfaz para observadores
* `Subject`: Interfaz para sujetos observables
* `Customer`: Observador concreto (cliente que recibe notificaciones)
* `OrderSystem`: Sujeto concreto (sistema que notifica cambios)

**Ventajas:**

* Desacoplamiento entre el sistema de pedidos y los clientes
* Fácil agregar o remover clientes sin modificar el sistema
* Los clientes se suscriben/desuscriben dinámicamente
* Cumple con el principio de Inversión de Dependencias (DIP)

**Ejemplo de uso:**

```python
order_system = OrderSystem()
customer = Customer("Juan")
order_system.attach(customer)
order_system.notify_all_ready()  # Juan recibe la notificación
```

### 3. Patrón Command

**Razón de uso:** El patrón Command encapsula una solicitud como un objeto, permitiendo parametrizar clientes con diferentes solicitudes, encolar o registrar solicitudes, y soportar operaciones que pueden deshacerse.

**Implementación:**

* En el archivo `CommandPattern.py`
* `Command`: Interfaz para comandos
* `OrderCommand`: Comando concreto para realizar pedidos
* `PrepareCommand`: Comando concreto para preparar items

**Ventajas:**

* Encapsula las acciones de ordenar y preparar como objetos
* Permite almacenar historial de comandos (útil para auditoría)
* Desacopla quien invoca la acción de quien la ejecuta
* Fácilmente extensible para agregar nuevos tipos de comandos (ej: cancelar pedido)
* Permite implementar operaciones de deshacer/rehacer en el futuro

**Ejemplo de uso:**

```python
order_cmd = OrderCommand(customer, item, "bebida")
order_cmd.execute()  # Ejecuta el pedido
```

## Buenas Prácticas de Ingeniería de Software Aplicadas

### 1. Principios SOLID

**Single Responsibility Principle (SRP):**

* Cada clase tiene una única responsabilidad claramente definida
* `Beverage` solo representa bebidas, decoradores solo agregan extras específicos
* `Customer` solo maneja información y notificaciones del cliente
* `OrderCommand` solo encapsula un pedido

**Open/Closed Principle (OCP):**

* Las clases están abiertas a extensión pero cerradas a modificación
* Nuevos decoradores pueden agregarse sin modificar código existente
* Nuevos tipos de comandos pueden crearse extendiendo `Command`

**Liskov Substitution Principle (LSP):**

* Los decoradores pueden sustituir a `MenuItem` sin problemas
* Los observadores concretos pueden sustituir a `Observer`

**Interface Segregation Principle (ISP):**

* Interfaces pequeñas y específicas (`Observer`, `Subject`, `Command`)
* Los clientes solo dependen de métodos que realmente usan
* `_add_extra()` en `MenuItemDecorator` es opcional para decoradores que no lo necesitan

**Dependency Inversion Principle (DIP):**

* Las clases dependen de abstracciones (interfaces), no de concreciones
* `OrderSystem` depende de `Observer`, no de `Customer` directamente

### 2. Código Limpio y Mantenible

**Nombres descriptivos:**

* Clases, métodos y variables tienen nombres claros que expresan su propósito
* `MilkDecorator`, `OrderCommand`, `notify_all_ready()`

**Documentación:**

* Docstrings en todas las clases y métodos principales
* Comentarios que separan secciones lógicas del código

**Type hints:**

* Uso de type hints de Python para mejorar legibilidad y detectar errores
* `def get_description(self) -> str:`
* `order_commands: List[OrderCommand]`

**Abstracción:**

* Uso apropiado de clases abstractas (`ABC`) para definir contratos
* Métodos abstractos fuerzan implementación en subclases

### 3. Separación de Responsabilidades

**Modularización:**

* Código organizado en secciones lógicas y archivos claramente delimitadas
* Patrones separados en secciones distintas de los archivos

**Encapsulación:**

* Atributos con prefijo `_` como convención para indicar que son internos/privados
* Acceso controlado mediante métodos públicos

### 4. Extensibilidad

El diseño permite fácilmente:

* Agregar nuevos tipos de bebidas o alimentos
* Agregar nuevos decoradores para extras
* Agregar nuevos tipos de trabajadores
* Agregar nuevos comandos (cancelar, modificar pedido)
* Agregar nuevos tipos de observadores

### 5. Testing y Mantenibilidad

**Bajo acoplamiento:**

* Las clases están débilmente acopladas, facilitando pruebas unitarias
* Cada componente puede probarse independientemente

**Alta cohesión:**

* Cada clase agrupa funcionalidades relacionadas
* Facilita el mantenimiento y comprensión del código

## Estructura del Proyecto

```txt
swdesign-tarea4/
├── src/
│   ├── CommandPattern.py      # Implementación del patrón Command
│   ├── DecoratorPattern.py    # Implementación del patrón Decorator
│   ├── ObserverPattern.py     # Implementación del patrón Observer
│   ├── Worker.py              # Clases base y concretas de trabajadores
│   └── main.py                # Punto de entrada y simulación del sistema
├── README.md                  # Este archivo
└── LICENSE
```

## Ejecución

```bash
python src/main.py
```

### Salida Esperada

```txt
=== Coffee Shop Simulation ===

Customer: Juan
Orders a Coffee with milk, cream and cinnamon
Orders a Muffin with chocolate filling and caramel topping

Customer: Mary
Orders a Green tea
Orders a Double espresso coffee with cream
Orders a Sandwich with ham and cheese filling


[Barista]: Preparing beverage: Coffee with milk, cream and cinnamon
[Baker]: Preparing food: Muffin with chocolate filling and caramel topping
[Barista]: Preparing beverage: Green tea
[Barista]: Preparing beverage: Double espresso coffee with cream
[Baker]: Preparing food: Sandwich with ham and cheese filling

[System]: Customers are notified when their orders are ready.
```

## Decisiones de Diseño Importantes

### Patrones elegidos

* **Decorator**: Es el ideal para agregar funcionalidades extra a objetos ya existentes sin modificar su estructura.
* **Observer**: Perfecto para el sistema de notificaciones, permitiendo que los clientes se suscriban y reciban actualizaciones automáticamente.
* **Command**: Encapsula las solicitudes de pedidos y preparaciones, desacoplando invocadores y ejecutores.

## Licencia

Este proyecto está bajo la Licencia MIT.
