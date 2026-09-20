# Importa la clase base Vehiculo desde el módulo vehiculo
from vehiculo import Vehiculo

# Definición de la clase Auto que hereda de la clase base Vehiculo
class Auto(Vehiculo):

    # Sobrescribe el método tarifa_hora para devolver la tarifa específica de un automóvil
    def tarifa_hora(self) -> int:
        # Retorna el valor entero 25000 como tarifa por hora para autos
        return 25000
