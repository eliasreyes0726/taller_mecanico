# Taller Mecánico

Proyecto para el desarrollo e implementación del modelo completo de gestión y funcionamiento de un taller mecánico.

## Información Académica

- **Módulo:** Programación Orientada a Objetos Seguro
- **Periodo:** Segundo Semestre, 2026

## Descripción del Proyecto

Este repositorio contiene el modelado orientado a objetos para el sistema integral de un taller mecánico, aplicando principios de diseño seguro, buenas prácticas de desarrollo y patrones de arquitectura limpia.

El modelo contempla entidades y flujos clave como:
- Gestión de clientes y vehículos.
- Órdenes de trabajo, diagnósticos y reparaciones.
- Control de inventario de repuestos e insumos.
- Asignación de tareas a mecánicos y personal técnico.
- Facturación, garantías y reportes de servicio.

---

## Bitácora de Commits (Evolución del Proyecto)

A continuación se detalla la secuencia del desarrollo evolutivo del proyecto (1 prompt = 1 modificación = 1 commit):

| # | Commit | Descripción del Cambio |
|---|--------|------------------------|
| 1 | `64a8d6d` | **Commit Inicial:** Creación del repositorio y `README.md` explicativo del módulo. |
| 2 | `49b4822` | **Ajuste README:** Corrección tipográfica en el nombre del módulo en el `README.md`. |
| 3 | `b372902` | **Prompt 2:** Creación de la clase `Vehiculo` vacía (`pass`) en `vehiculo.py` con comentario base. |
| 4 | `4b0552a` | **Prompt 3:** Declaración de atributos `patente: str`, `anio: int` y `_en_taller: bool`. |
| 5 | `ce0caf7` | **Prompt 4:** Implementación del constructor `__init__` con `_en_taller = False` y comentarios línea por línea. |
| 6 | `02704dd` | **Prompt 5:** Creación de `main.py` para instanciar un vehículo (`KXPR84`, 2019) e imprimir sus atributos. |
| 7 | `00dd699` | **Prompt 6:** Métodos `ingresar()` y `entregar()` en `vehiculo.py` y pruebas en `main.py`. |
| 8 | `af72930` | **Prompt 7:** Encapsulamiento privado (`__`), eliminación de variables fuera del constructor y creación de getters tradicionales. |
| 9 | `6bf4ff7` | **Prompt 8:** Pruebas en `main.py` de los métodos getters tradicionales. |
| 10 | `81710b9` | **Prompt 9:** Refactorización a `@property` (`patente`, `anio`, `en_taller`) comentando su uso. |
| 11 | `ceb6987` | **Prompt 10:** Pruebas en `main.py` instanciando `v1` y `v2`, ingresando solo `v1` e imprimiendo con `@property`. |
| 12 | `1de2d1f` | **Prompt 11:** Implementación del método `tarifa_hora()` en `Vehiculo` retornando el valor entero `5000`. |
| 13 | `798d34a` | **Prompt 12:** Creación de las subclases `Auto`, `Moto` y `Camion` (heredando de `Vehiculo`) y actualización de `main.py`. |
| 14 | `6d40639` | **Prompt 13:** Adición del atributo privado `__capacidad_carga`, constructor con `super()` y getter `@property` en `Camion`. |
