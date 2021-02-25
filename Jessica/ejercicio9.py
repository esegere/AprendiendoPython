# En el siguiente ejercicio replicaremos el comportamiento del programa del ejercicio4
#
# Pero esta vez usaremos la funcion reduce del modulo functools
# para poder hacer las operaciones
#
# De la misma forma, usaremos decoradores para saber en que momento llamar las funciones
# estos decoradores se encuentran en la clase FunctionHandler del modulo utilidades.cli

from functools import reduce
from utilidades.cli import FunctionHandler

MENU = '''
    OPCIONES:
        1) Sumarlo todo
        2) Multiplicarlo todo
        3) Imprimirlo todo
        4) Salir del programa
'''


# fin de la zona de definición de menú
# defina aquí sus funciones

def seleccionar_opcion():
    print(MENU)
    return input("Ingrese una opción: ")


func_handler = FunctionHandler(loop_function=seleccionar_opcion)


@func_handler.call_when("1")
def sumar_todos(*numeros):
    resultado = reduce(lambda a, b: a + b, numeros)
    print(resultado)


@func_handler.call_when("2")
def multiplicar_todos(*numeros):
    resultado = reduce(lambda a, b: a * b, numeros)
    print(resultado)


@func_handler.call_when("3")
def imprimir_todos(*numeros):
    for numero in numeros:
        print(numero)


@func_handler.call_default
def imprimir_error():
    print("\n Opcion no valida")


# fin de la zona de definición de funciones
# no modificar la siguiente sección del programa

if __name__ == '__main__':
    number_list = tuple(
        float(number)
        for number in input("ingrese una lista de números separados por coma: ").strip(" ").split(",")
    )
    func_handler.function_parameters = number_list
    func_handler.loop_until("4")
