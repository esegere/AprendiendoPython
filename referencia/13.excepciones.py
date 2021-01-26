# las excepciones son errores que se producen en tiempo de ejecución
# estas provocan que el programa se detenga si no se controlan
# las excepciones son causadas por comportamientos inesperados en el programa
# de los cuales el programa mismo no se puede recuperar por si mismo si no se le ha programado para ello

def numeric_fail():
    return 500 / 0


def cast_fail():
    return int('palabras')


def access_fail():
    lista = [1, 2, 3]
    return lista[8]


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
    numeric_fail()
    cast_fail()
    access_fail()
