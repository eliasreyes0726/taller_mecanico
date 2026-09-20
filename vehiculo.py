# Esta clase representa el molde para la gestión de vehículos en el taller mecánico.

# Definición de la clase Vehiculo
class Vehiculo:

    # Constructor que inicializa los atributos privados del vehículo
    def __init__(self, patente: str, anio: int):
        # Asigna la patente pasada por parámetro al atributo privado __patente
        self.__patente = patente
        # Asigna el año pasado por parámetro al atributo privado __anio
        self.__anio = anio
        # Inicializa el atributo privado __en_taller siempre en False
        self.__en_taller = False

    # Método para registrar el ingreso del vehículo al taller mecánico
    def ingresar(self):
        # Cambia el atributo privado __en_taller a True
        self.__en_taller = True

    # Método para registrar la entrega del vehículo al cliente
    def entregar(self):
        # Cambia el atributo privado __en_taller a False
        self.__en_taller = False

    # El decorador @property permite acceder a este método getter como si fuera un atributo de solo lectura (sin usar paréntesis)
    @property
    def patente(self):
        # Retorna el valor del atributo privado __patente
        return self.__patente

    # El decorador @property convierte el método en una propiedad getter de solo lectura para el año del vehículo
    @property
    def anio(self):
        # Retorna el valor del atributo privado __anio
        return self.__anio

    # El decorador @property transforma la función en una propiedad getter para consultar si está en el taller
    @property
    def en_taller(self):
        # Retorna el valor del atributo privado __en_taller
        return self.__en_taller

    # Método que retorna la tarifa por hora de reparación de un vehículo
    def tarifa_hora(self) -> int:
        # Retorna el valor entero 5000 como costo por hora de reparación
        return 5000
