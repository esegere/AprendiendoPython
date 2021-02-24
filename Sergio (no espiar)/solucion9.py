# En el siguiente ejercicio replicaremos el comportamiento del programa del ejercicio4
#
# Pero esta vez usaremos la función reduce del modulo functools
# para poder hacer las operaciones
#
# De la misma forma, usaremos decoradores para saber en que momento llamar las funciones
# estos decoradores se encuentran en la clase FunctionHandler del modulo utilidades.cli

from functools import reduce
from operator import mul

from utilidades.cli import FunctionHandler

MENU_9 = '''
    OPCIONES:
        1) Sumarlo todo
        2) Multiplicarlo todo
        3) Imprimirlo todo
        4) Salir
'''


def selecciona_opcion():
    print(MENU_9)
    return input("ingrese una opción: ")


func_handler = FunctionHandler(loop_function=selecciona_opcion)


@func_handler.call_when("1")
def imprimir_sumar_todos(*numeros):
    print(f"la suma de los números es: {sum(numeros)}")


@func_handler.call_when("2")
def imprimir_multiplicar_todos(*numeros):
    print(f"la multiplicación de los números es: {reduce(mul, numeros)}")


@func_handler.call_when("3")
def imprimir_todos(*numeros):
    for numero in numeros:
        print(numero)


@func_handler.call_default
def imprimir_error():
    print("\n Opcion invalida")


if __name__ == '__main__':
    number_list = tuple(
        float(number)
        for number in input("ingrese una lista de números separados por coma: ").strip(" ").split(",")
    )
    func_handler.function_parameters = number_list
    func_handler.loop_until("4")
