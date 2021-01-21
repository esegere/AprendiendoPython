# crear un programa que pida una lista de números al usuario desde la linea de comandos
# cada numero debera ir separado por una coma ","
# después de ingresar su lista de números al usuario se le pedirá que elija
# entre 4 opciones
# 1) quiere sumarlos todos
# 2) quiere multiplicarlos todos
# 3) quiere imprimirlos todos
# 4) quiere salir del programa
#
# si el usuario teclea una opción incorrecta mandar el mensaje "opción no valida"
#
# el programa principal estará codificado, solamente deberán escribirse las funciones:
# "sumar_todos"
#       esta función debe regresar la suma de los números (un número)
# "multiplicar_todos"
#       esta función debe regresar la multiplicación de los números (un número)
# "imprimir_todos"
#       No regresa nada
# "imprimir_error"
#       No regresa nada
#
# defina aquí el mensaje donde se muestran las opciones (Menu de opciones)
MENU = '''
    OPCIONES:
        1) Sumarlo todo
        2) Multiplicarlo todo
        3) Imprimirlo todo
        4) Salir del programa
'''


# fin de la zona de definición de menú
# defina aquí sus funciones
def sumar_todos(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    return resultado


def multiplicar_todos(*numeros):
    resultado = 1
    for numero in numeros:
        resultado *= numero
    return resultado


def imprimir_todos(*numeros):
    for numero in numeros:
        print(numero)


def imprimir_error():
    print("\n Opcion no valida")


# fin de la zona de definición de funciones
# no modificar la siguiente sección del programa

if __name__ == '__main__':
    number_list = tuple(
        float(number)
        for number in input("ingrese una lista de números separados por coma: ").strip(" ").split(",")
    )
    while True:
        print(MENU)
        option = input("ingrese una opción")
        if option == "1":
            print(f"la suma de los números es: {sumar_todos(*number_list)}")
        elif option == "2":
            print(f"la multiplicación de los números es: {multiplicar_todos(*number_list)}")
        elif option == "3":
            imprimir_todos(*number_list)
        elif option == "4":
            break
        else:
            imprimir_error()
