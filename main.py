# Importa la clase Vehiculo desde el módulo vehiculo.py
from vehiculo import Vehiculo

# Instancia el primer vehículo (v1) con patente 'KXPR84' y año 2019
v1 = Vehiculo(patente="KXPR84", anio=2019)

# Instancia el segundo vehículo (v2) con patente 'JKLM12' y año 2016
v2 = Vehiculo(patente="JKLM12", anio=2016)

# Registra el ingreso al taller únicamente para el primer vehículo (v1)
v1.ingresar()

# Imprime la patente del primer vehículo v1 usando su propiedad @property
print(f"Vehículo v1 - Patente: {v1.patente}")

# Imprime si el primer vehículo v1 está en el taller usando su propiedad @property
print(f"Vehículo v1 - ¿Está en el taller?: {v1.en_taller}")

# Imprime la tarifa por hora de reparación del vehículo v1 llamando al método tarifa_hora()
print(f"Vehículo v1 - Tarifa por hora: ${v1.tarifa_hora()}")

# Imprime la patente del segundo vehículo v2 usando su propiedad @property
print(f"Vehículo v2 - Patente: {v2.patente}")

# Imprime si el segundo vehículo v2 está en el taller usando su propiedad @property
print(f"Vehículo v2 - ¿Está en el taller?: {v2.en_taller}")
