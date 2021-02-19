# construir un programa que acepte una cadena de texto como argumento
# cuente las palabras diferentes que tiene el texto e imprima cada una de ellas
# junto con su cantidad de ocurrencias
#
# para hacer el conteo, use la clase Counter del modulo collections
#

from sys import argv as parametros
from collections import Counter


def validar_parametro(parametro):
    return len(parametro) == 2


def contar_palabras(parametro):
    contador = Counter(parametro.replace(",", "").split(" "))
    for palabra, veces in contador.items():
        print(f"{palabra}: {veces}")


if __name__ == '__main__':
    if validar_parametro(parametros):
        contar_palabras(parametros[1])
    else:
        print("no puedo we :´c")
