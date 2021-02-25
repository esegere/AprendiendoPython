# En el siguiente ejercicio replicaremos el comportamiento del programa del ejercicio4
#
# Pero esta vez usaremos la funcion reduce del modulo functools
# para poder hacer las operaciones
#
# De la misma forma, usaremos decoradores para saber en que momento llamar las funciones
# estos decoradores se encuentran en la clase FunctionHandler del modulo utilidades.cli

from functools import reduce

from utilidades.cli import FunctionHandler

MENU = """
  MENU DE OPCIONES
  1.- SUMAR
  2.- MULTIPLICAR
  3.- QUIERE SUPRIMIR TODOS
  4.-QUIERE SALIR DEL PROGRAMA
  5.-ERROR
  

"""


def selecciona_opcion():
    print(MENU)
    return input("Ingrese una opcion:")


func_handler = FunctionHandler(loop_function=selecciona_opcion)


# fin de la zona de definición de menú
# defina aquí sus funciones

@func_handler.call_when("1")
def sumar_todos(*numeros):
    resultado = reduce(lambda x, y: x + y, numeros)
    print(resultado)


@func_handler.call_when("2")
def multiplicar_todos(*numeros):
    resultado = reduce(lambda x, y: x * y, numeros)
    print(resultado)


@func_handler.call_when("3")
def imprimir_todos(*numeros):
    for numero in numeros:
        print(numero)


@func_handler.call_default
def imprimir_error():
    print("Opcion no Valida")


# fin de la zona de definición de funciones
# no modificar la siguiente sección del programa

if __name__ == '__main__':
    number_list = tuple(
        float(number)
        for number in input("ingrese una lista de números separados por coma: ").strip(" ").split(",")

    )
    func_handler.function_parameters = number_list
    func_handler.loop_until("4")
