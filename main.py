# Importa la clase Vehiculo desde el módulo vehiculo
from vehiculo import Vehiculo

# Crea un objeto de la clase Vehiculo con patente 'KXPR84' y año 2019
auto = Vehiculo(patente="KXPR84", anio=2019)

# Muestra en consola la patente usando el método getter obtener_patente()
print(f"Patente: {auto.obtener_patente()}")

# Muestra en consola el año usando el método getter obtener_anio()
print(f"Año: {auto.obtener_anio()}")

# Muestra en consola el estado inicial usando el método getter esta_en_taller()
print(f"Estado inicial ¿Está en el taller?: {auto.esta_en_taller()}")

# Llama al método ingresar() para registrar la entrada del vehículo al taller
auto.ingresar()

# Muestra en consola el estado del vehículo tras llamar a ingresar()
print(f"Después de ingresar() ¿Está en el taller?: {auto.esta_en_taller()}")

# Llama al método entregar() para registrar la salida del vehículo del taller
auto.entregar()

# Muestra en consola el estado del vehículo tras llamar a entregar()
print(f"Después de entregar() ¿Está en el taller?: {auto.esta_en_taller()}")
