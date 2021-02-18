# las excepciones son errores que se producen en tiempo de ejecución
# estas provocan que el programa se detenga si no se controlan
# las excepciones son causadas por comportamientos inesperados en el programa
# de los cuales el programa mismo no se puede recuperar por si mismo si no se le ha programado para ello

def numeric_fail(numero):
    resultado = 0
    try:
        resultado = 500 / numero
    except ZeroDivisionError:
        resultado = 0
    else:
        print("todo salio bien")
    finally:
        return resultado


def cast_fail():
    try:
        return int('palabras')
    except ValueError:
        return 1


def access_fail():
    lista = [1, 2, 3]
    try:
        return lista[8]
    except IndexError:
        return 0


# para controlar las excepciones tenemos las estructuras:
#       try-except
#       try=except-finally
#       try-except-else-finally
#
# dentro del bloque try se coloca el código que puede ocasionar una excepción
#
# dentro del bloque except se coloca el código a ejecutar en acaso de que una excepción surja
# se pueden incluir tantos bloques except como excepciones se quieran controlas individualmente
#
# el bloque else es opcional, aquí se coloca código que solo se ejecutará si no se presento ninguna excepción
#
# así mismo, el bloque finally es opcional y aquí se incluye el código que se debe ejecutar
# independientemente de si hubo o no una excepción, normalmente se suelen liberar recursos

if __name__ == '__main__':
    access_fail()
    cast_fail()
    numeric_fail(0)
