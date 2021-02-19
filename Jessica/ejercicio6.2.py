# crear un programa que pida al usuario un carácter
# después pida un numero (ancho)
# después otro numero (alto)
#
# el programa después debera
# imprimir un rectángulo usando ese carácter, con las medidas que se le especificaron
#
# al pedir los datos el programa debera validar:
#
#       - que solo sea un carácter el especificado,
#       si se reciben mas, pedir al usuario nuevamente el dato,
#       asi, sucesivamente hasta que sea solo un carácter
#
#       - que el ancho sea un numero entero
#       de no ser un numero entero, pedir el dato de nuevo al usuario
#
#       - que el alto sea un numero entero
#       de no ser un numero entero, pedir el dato de nuevo al usuario
#
#
# ejemplo:
#
#   carácter: *
#   ancho: 5
#   alto: 3
#
#   *****
#   *****
#   *****
def pedir_caracter():
    while True:
        caracter = input("Ingrese un caracter: ")
        if validar_caracter(caracter):
            return caracter
        else:
            print("Ingreso mas de un caracter")


def validar_caracter(caracter):
    return len(caracter) == 1


def pedir_dimension(direccion):
    while True:
        try:
            dimension = int(input(f"Ingrese el {direccion}: "))
        except ValueError:
            print("No ingreso un numero entero")
        else:
            return dimension


def imprimir_forma(caracter, ancho, alto):
    print(caracter * ancho)


if __name__ == '__main__':
    pedir_caracter()
    pedir_dimension("ancho")
    pedir_dimension("alto")
    print(imprimir_forma())
