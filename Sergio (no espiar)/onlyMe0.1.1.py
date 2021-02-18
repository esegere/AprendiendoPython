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
from statistics import mean
from collections import Counter

INSTRUCCIONES = "ingresa una lista de números separados por coma:\n"


def imprimir(func):
    def wrapper(*args):
        print(f"{func.__name__} ", end="")
        return func(*args)

    return wrapper


@imprimir
def promedio(*numeros):
    return mean(numeros)


@imprimir
def moda(*numeros):
    counter = Counter(numeros)
    number, _ = counter.most_common(1).pop()
    return number


@imprimir
def maximo(*numeros):
    return max(numeros)


@imprimir
def minimo(*numeros):
    return min(numeros)

@imprimir
def suma(*numeros):
    return sum(numeros)


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
    print(f"{promedio(*numeros)}")
    print(f"{moda(*numeros)}")
    print(f"{maximo(*numeros)}")
    print(f"{minimo(*numeros)}")
    print(f"{suma(*numeros)}")
