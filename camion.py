# Importa la clase base Vehiculo desde el módulo vehiculo
from vehiculo import Vehiculo

# Definición de la clase Camion que hereda de la clase base Vehiculo
class Camion(Vehiculo):

    # Constructor de Camion que recibe patente, año y capacidad de carga en kilos
    def __init__(self, patente: str, anio: int, capacidad_carga: int):
        # Llama al constructor de la clase padre (Vehiculo) para inicializar patente y año
        super().__init__(patente, anio)
        # Guarda la capacidad de carga en kilos como atributo privado __capacidad_carga
        self.__capacidad_carga = capacidad_carga

    # Decorador @property para crear el getter del atributo privado capacidad_carga
    @property
    def capacidad_carga(self) -> int:
        # Retorna el valor del atributo privado __capacidad_carga
        return self.__capacidad_carga
