from planetas import Planeta, PlanetaConcordia, PlanetaIlum, PlanetaKamino

class EstrellaDeLaMuerte:
    def __init__(self):
        self.puntos_vida = 1000

    def destruir_planeta(self, planeta):
        if planeta.volumen <= self.puntos_vida:
            print(f"La Estrella de la Muerte ha destruido el planeta {planeta.nombre}.")
            self.puntos_vida -= planeta.volumen
            print(f"a {planeta.nombre} le quedan {self.puntos_vida} puntos")
        else:
            print(f"No se puede destruir el planeta {planeta.nombre}. La Estrella de la Muerte no tiene suficientes puntos de vida.")

if __name__ == "__main__":
    estrella_muerte = EstrellaDeLaMuerte()
    planeta_concordia = PlanetaConcordia()
    planeta_ilum = PlanetaIlum()
    planeta_kamino = PlanetaKamino()

    estrella_muerte.destruir_planeta(planeta_concordia)
    estrella_muerte.destruir_planeta(planeta_ilum)
    estrella_muerte.destruir_planeta(planeta_kamino)
