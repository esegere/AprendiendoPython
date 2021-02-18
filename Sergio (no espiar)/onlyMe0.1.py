# realizar un programa que calcule:
#   - promedio
#   - moda
#   - valor maximo
#   - valor mínimo
#
# el programa debe pedir una lista de números separados por coma desde la linea de comandos
# y regresar los resultados de todas las operaciones
#
# en caso de que el usuario ingrese un dato invalido, informarle que solo deben ser números

INSTRUCCIONES = "ingresa una lista de números separados por coma:\n"


def promedio(*numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    return suma / len(numeros)


def moda(*numeros):
    conteos = {}
    for numero in numeros:
        if numero in conteos.keys():
            conteos[numero] += 1
        else:
            conteos[numero] = 1
    maximo_ocurrencias = 0
    for ocurrencia in conteos.values():
        if ocurrencia > maximo_ocurrencias:
            maximo_ocurrencias = ocurrencia
    numero_seleccionado = None
    for numero in conteos.keys():
        if conteos[numero] == maximo_ocurrencias:
            numero_seleccionado = numero
    return numero_seleccionado


def maximo(*numeros):
    lista = list(numeros)
    lista.sort()
    return lista[len(lista) - 1]


def minimo(*numeros):
    lista = list(numeros)
    lista.sort()
    return lista[0]


if __name__ == '__main__':
    while True:
        try:
            numeros = tuple(
                float(i) for i in input(INSTRUCCIONES).strip(" ").split(",")
            )
        except ValueError:
            print("solo se permiten numeros")
        else:
            break
    print(f"promedio: {promedio(*numeros)}")
    print(f"moda: {moda(*numeros)}")
    print(f"maximo: {maximo(*numeros)}")
    print(f"minimo: {minimo(*numeros)}")
