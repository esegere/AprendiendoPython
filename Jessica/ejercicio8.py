# escriba un programa qué acepte como argumento una cadena de texto
# y transforme la cadena de acuerdo a las siguientes banderas
#
# -r        invierta la cadena de texto
# -fN       imprima solo las primeras N letras de la cadena
# -lN       imprimir solo las ultimas N letras de la cadena

from sys import argv as parametros


def invertir_cadena(parametro):
    return parametro[::-1]


def imprimir_primeras(parametro, numero):
    return parametro[:numero]


def imprimir_ultimas(parametro, numero):
    return parametro[-numero:]


if __name__ == '__main__':
    if parametros[1] == "-r":
        print(invertir_cadena(parametros[2]))
    elif parametros[1][:2] == "-f":
        numero = int(parametros[1][2:])
        print(imprimir_primeras(parametros[2], numero))
    elif parametros[1][:2] == "-l":
        numero = int(parametros[1][2:])
        print(imprimir_ultimas(parametros[2], numero))
    else:
        print("tú eres invalido")
