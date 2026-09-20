# Importa la clase base Vehiculo desde el módulo vehiculo
from vehiculo import Vehiculo

# Definición de la clase Moto que hereda de la clase base Vehiculo
class Moto(Vehiculo):

    # Sobrescribe el método tarifa_hora para devolver la tarifa específica de una motocicleta
    def tarifa_hora(self) -> int:
        # Retorna el valor entero 15000 como tarifa por hora para motos
        return 15000
