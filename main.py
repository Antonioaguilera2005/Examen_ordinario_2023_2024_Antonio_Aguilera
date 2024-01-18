from estrella_de_la_muerte_2 import Estrella_de_la_muerte
from naves import NavePequena, NaveGrande

if __name__ == "__main__":
    estrella_muerte = EstrellaDeLaMuerte()
    nave_pequena = NavePequena("X-Wing", 150)
    nave_grande = NaveGrande("Star Destroyer", 800)

    estrella_muerte.atacar_nave_aliada(nave_pequena)
    estrella_muerte.atacar_nave_aliada(nave_grande)
