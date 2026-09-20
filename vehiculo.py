# Esta clase representa solo el molde base para la gestión de vehículos en el taller mecánico.

class Vehiculo:
    patente: str
    anio: int
    _en_taller: bool

    # Constructor que inicializa los atributos del vehículo
    def __init__(self, patente: str, anio: int):
        # Guarda la patente pasada por argumento en el atributo patente
        self.patente = patente
        # Guarda el año pasado por argumento en el atributo anio
        self.anio = anio
        # Inicializa siempre en False porque un vehículo nuevo no ingresa estando en el taller
        self._en_taller = False
