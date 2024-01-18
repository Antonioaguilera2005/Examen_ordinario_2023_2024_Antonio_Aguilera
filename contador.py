import time

def blitz_chess():
    tiempo_carlsen = 180  # 3 minutos en segundos
    tiempo_nakamura = 180  # 3 minutos en segundos
    tiempo_movimiento = 10  # Tiempo inicial por movimiento en segundos

    turno_actual = "Carlsen"

    while tiempo_carlsen > 0 and tiempo_nakamura > 0:
        print(f"\nTiempo actual - Carlsen: {tiempo_carlsen} segundos | Nakamura: {tiempo_nakamura} segundos")
        print(f"Turno de {turno_actual}")

        movimiento = input("Ingrese el nombre del jugador que realiza el movimiento (Carlsen/Hikaru) o 'Salir' para terminar: ")

        if movimiento.lower() == "salir":
            print("La partida ha sido interrumpida.")
            break

        if (turno_actual == "Carlsen" and movimiento.lower() == "carlsen") or (turno_actual == "Hikaru" and movimiento.lower() == "hikaru"):
            tiempo_actual = tiempo_carlsen if turno_actual == "Carlsen" else tiempo_nakamura
            tiempo_actual -= tiempo_movimiento

            if tiempo_actual < 60 and tiempo_movimiento == 10:
                tiempo_movimiento = 5
                print("¡Se ha reducido el tiempo por movimiento a 5 segundos!")

            turno_actual = "Hikaru" if turno_actual == "Carlsen" else "Carlsen"

            if tiempo_actual <= 0:
                print(f"¡{turno_actual} se ha quedado sin tiempo! ¡{turno_actual} pierde la partida!")
                break

            if turno_actual == "Carlsen":
                tiempo_carlsen = tiempo_actual
            else:
                tiempo_nakamura = tiempo_actual
        else:
            print("Nombre de jugador incorrecto. Inténtalo de nuevo.")

    if tiempo_carlsen <= 0 and tiempo_nakamura <= 0:
        print("\n¡La partida ha terminado en empate!")
    else:
        ganador = "Carlsen" if tiempo_carlsen > tiempo_nakamura else "Hikaru"
        print(f"\n¡La partida ha terminado! ¡{ganador} es el ganador!")

if __name__ == "__main__":
    blitz_chess()
