# escriba un programa qué acepte como argumento una cadena de texto
# y transforme la cadena de acuerdo a las siguientes banderas
#
# -r        invierta la cadena de texto
# -fN       imprima solo las primeras N letras de la cadena
# -lN       imprimir solo las ultimas N letras de la cadena

from sys import argv as banderas


def invertir_cadena_de_texto(cadena):
    print(cadena[::-1])

def imprimir_primeras_n_letras(cadena,N):
    print(cadena[0:N])

def imprimir_ultimas_n_letras(cadena,N):
    print(cadena[-N:])

if __name__ == '__main__':


    if banderas[1]=="-r":
      invertir_cadena_de_texto(banderas[2])

    elif banderas[1][:2]=="-f":
      numero=int(banderas[1][2:])
      imprimir_primeras_n_letras(banderas[2],numero)
    elif banderas[1][:2]=="-l":
      numero=int(banderas[1][2:])
      imprimir_ultimas_n_letras(banderas[2],numero)

    else:
      print("Opcion no valida :(")


