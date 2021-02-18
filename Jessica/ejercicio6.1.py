# escriba un programa que pida al usuario una lista de números enteros separados por coma
#               similar al ejercicio 4
# después ofrezca las siguientes opciones
#
# 1) imprimir números pares
# 2) imprimir números impares
# 3) imprimir números primos
# 4) salir
#
# como siempre, si se selecciona una opción invalida, mostrar el mensaje "opción no valida"

MENU = '''
    OPCIONES:
        1) Imprimir números pares
        2) Imprimir números impares
        3) Imprimir números primos  
        4) Salira
'''


def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


def calcular_numeros_pares(*number_list):
    lista_pares = []
    for numero in number_list:
        if es_par(numero):
            lista_pares.append(numero)
    return lista_pares


def calcular_numeros_impares(*number_list):
    lista_impares = []
    for numero in number_list:
        if not es_par(numero):
            lista_impares.append(numero)
    return lista_impares


def es_primo(numero):
    contador_divisores = 0
    for i in range(1, numero):
        if numero % i == 0:
            contador_divisores += 1
    if contador_divisores == 1:
        return True
    else:
        return False

def calcular_numeros_primos(*number_lis):
    lista_primos = []
    for numero in number_lis:
        if es_primo(numero):
            lista_primos.append(numero)
    return lista_primos


def imprimir_error():
    print("\n Opcion no valida")


if __name__ == '__main__':
    try:
        number_list = tuple(
            int(number)
            for number in input("ingrese una lista de números separados por coma: ").strip(" ").split(",")
        )
    except ValueError:
        print("los elementos que ingresaste no contienen unicamente numeros")
        exit()
    while True:
        print(MENU)
        option = input("Ingrese una opción: ")
        if option == "1":
            print(f"Números pares: {calcular_numeros_pares(*number_list)}")
        elif option == "2":
            print(f"Números impares: {calcular_numeros_impares(*number_list)}")
        elif option == "3":
            print(f"Números primos: {calcular_numeros_primos(*number_list)}")
        elif option == "4":
            break
        else:
            imprimir_error()