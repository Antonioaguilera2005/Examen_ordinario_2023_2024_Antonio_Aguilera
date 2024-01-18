from enum import Enum

class Planeta:
    def __init__(self, nombre, volumen, clasificacion):
        self.nombre = nombre
        self.volumen = volumen
        self.clasificacion = clasificacion

class ClasificacionPlanetaria(Enum):
    Concordia = 500
    Ilum = 1200
    Kamino = 800

class PlanetaConcordia(Planeta):
    def __init__(self):
        super().__init__("Concordia", 500, ClasificacionPlanetaria.Concordia.value)

class PlanetaIlum(Planeta):
    def __init__(self):
        super().__init__("Ilum", 1200, ClasificacionPlanetaria.Ilum.value)

class PlanetaKamino(Planeta):
    def __init__(self):
        super().__init__("Kamino", 800, ClasificacionPlanetaria.Kamino.value)
