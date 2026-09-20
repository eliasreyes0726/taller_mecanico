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

    # Método para registrar el ingreso del vehículo al taller mecánico
    def ingresar(self):
        # Cambia el estado del atributo _en_taller a True para indicar que está en el taller
        self._en_taller = True

    # Método para registrar la entrega del vehículo al cliente
    def entregar(self):
        # Cambia el estado del atributo _en_taller a False para indicar que salió del taller
        self._en_taller = False
