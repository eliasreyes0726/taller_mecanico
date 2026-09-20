from vehiculo import Vehiculo

# Instanciación de un objeto Vehiculo con la patente 'KXPR84' y año 2019
auto = Vehiculo(patente="KXPR84", anio=2019)

# Mostrar la información del vehículo creado
print(f"Patente: {auto.patente}")
print(f"Año: {auto.anio}")
print(f"¿Está en el taller?: {auto._en_taller}")
