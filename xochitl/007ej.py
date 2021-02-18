# construir un programa que acepte una cadena de texto como argumento
# cuente las palabras diferentes que tiene el texto e imprima cada una de ellas
# junto con su cantidad de ocurrencias
#
# para hacer el conteo, use la clase Counter del modulo collections
#

from sys import argv as parametro
from collections import Counter

def validar_parametro(parametro):
    if len(parametro)>=2:
        return True
    else:
        print("el parametro no es correcto ya que solo se pueden validar las funciones de acuerdo a mayor que 2 valores :(")
        return False

def contar_palabras(parametro):
      contador=Counter(parametro.replace(",","").split(" "))
      for palabra, veces in contador.items():
       print(f"{palabra}:{veces}")

if __name__ == '__main__':
 if   validar_parametro(parametro):
      contar_palabras(parametro[1])



