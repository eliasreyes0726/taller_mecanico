# Importa la clase Auto desde el módulo auto.py
from auto import Auto
# Importa la clase Moto desde el módulo moto.py
from moto import Moto
# Importa la clase Camion desde el módulo camion.py
from camion import Camion

# Instancia un objeto de la clase Auto (hereda de Vehiculo)
mi_auto = Auto(patente="KXPR84", anio=2019)

# Instancia un objeto de la clase Moto (hereda de Vehiculo)
mi_moto = Moto(patente="JKLM12", anio=2021)

# Instancia un objeto de la clase Camion especificando patente, año y capacidad de carga en kilos
mi_camion = Camion(patente="TRCK99", anio=2018, capacidad_carga=5000)

# Imprime la patente y tarifa por hora del Auto
print(f"Auto - Patente: {mi_auto.patente}, Tarifa por hora: ${mi_auto.tarifa_hora()}")

# Imprime la patente y tarifa por hora de la Moto
print(f"Moto - Patente: {mi_moto.patente}, Tarifa por hora: ${mi_moto.tarifa_hora()}")

# Imprime la patente, tarifa por hora y capacidad de carga del Camión
print(f"Camión - Patente: {mi_camion.patente}, Tarifa por hora: ${mi_camion.tarifa_hora()}, Capacidad: {mi_camion.capacidad_carga} kg")
