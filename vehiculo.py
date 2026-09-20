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

    # Método público getter para obtener la patente del vehículo
    def obtener_patente(self):
        # Retorna el valor del atributo privado __patente
        return self.__patente

    # Método público getter para obtener el año del vehículo
    def obtener_anio(self):
        # Retorna el valor del atributo privado __anio
        return self.__anio

    # Método público getter para verificar si el vehículo está en el taller
    def esta_en_taller(self):
        # Retorna el valor del atributo privado __en_taller
        return self.__en_taller
