# construir un programa que acepte una cadena de texto como argumento
# cuente las palabras diferentes que tiene el texto e imprima cada una de ellas
# junto con su cantidad de ocurrencias
#
# para hacer el conteo, use la clase Counter del modulo collections
#

from sys import argv as parametros
from collections import Counter


def validar_parametro(parametro):
    try:
        parametro[1]
    except IndexError:
        print("Parametros incorrectos")
        return False
    else:
        return True


def contar_palabras(parametro):
    contador = Counter(parametro.replace(",", "").split(" "))
    for palabra, veces in contador.items():
        print(f"{palabra}: {veces}")


if __name__ == '__main__':
    if validar_parametro(parametros):
        contar_palabras(parametros[1])
