# Importa la clase Vehiculo desde el módulo vehiculo
from vehiculo import Vehiculo

# Crea un objeto de la clase Vehiculo con patente 'KXPR84' y año 2019
auto = Vehiculo(patente="KXPR84", anio=2019)

# Muestra en consola el estado inicial del vehículo recién creado
print(f"Estado inicial ¿Está en el taller?: {auto._en_taller}")

# Llama al método ingresar() para meter el vehículo al taller
auto.ingresar()

# Muestra en consola el estado del vehículo luego de llamar a ingresar()
print(f"Después de ingresar() ¿Está en el taller?: {auto._en_taller}")

# Llama al método entregar() para sacar el vehículo del taller
auto.entregar()

# Muestra en consola el estado del vehículo luego de llamar a entregar()
print(f"Después de entregar() ¿Está en el taller?: {auto._en_taller}")
