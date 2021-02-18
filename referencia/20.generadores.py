# los generadores son un tipo especial de función que puede pausar su ejecución
# devolver un valor y reanudar su ejecución después
#
# un generador se define igual a una función, pero en lugar de usar la clausula "return"
# se usa "yield" esta palabra permite devolver ese valor y pausar la ejecución
#
# estas funciones son especialmente útiles cuando se necesitan generar secuencias
# sobre las cuales iterar, estas secuencias podrían ser infinitas
#
# ejemplos de generadores es la función "range"
from random import choice


# este generador devuelve una palabra a la vez (al azar) de una lista dada
def generador(*palabras):
    while True:
        yield choice(palabras)


def saludar_a(nombre):
    print(f"hola {nombre}")


if __name__ == '__main__':
    gen = generador("yo", "tu")  # produce un generador almacenado en la variable gen
    primer_valor = next(gen)  # para poder extraer los elementos de la secuencia se usa la función next (uno a uno)
    segundo_valor = next(gen)
    # for nombre in generador("yo", "tu", "el", "ella"):
    #     saludar_a(nombre)
