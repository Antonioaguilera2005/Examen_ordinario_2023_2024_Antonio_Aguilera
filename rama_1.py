
def generar_piramide(n):
    valor = 0
    for i in range(1, n + 1):
        espacios = ((n - i) * " ")
        asteriscos = (i * "*")
        if len(asteriscos) == 1:
            print(espacios + asteriscos + espacios)
        else :
            valor += 1
            print(espacios + asteriscos + (valor * "*") + espacios)
def main():
    # utilizo el try except para evitar que el usuario indroduzca un número incorrecto, de esta manera condigo que no ssalgan errores y solo una frase diciedo que no es posible
    try:
        n = int(input("Ingrese un número entero mayor o igual a 1: "))
        if n < 1:
            print("Por favor, ingrese un número mayor o igual a 1.")
        else:
            generar_piramide(n)
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

if __name__ == "__main__":
    main()
