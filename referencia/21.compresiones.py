# la compresiones son una característica de python
# que permite crear algunas colecciones de forma descriptiva
# definiendo toda la colección en una sola instrucción de código
#
# la sintaxis es parecida a la del ciclo "for"
# pudiendo agregar también secciones de "if"
#
# expresion for elemento in colección/generador
# expresion for elemento in colección/generador if predicado

# existen 3 tipos de compresiones:

# compresión de listas, el tipo de compresión mas común
# sirve para crear una lista poblada con los elementos deseados
# por ejemplo, una lista con las primeras 10 potencias de 2 desde el 2

lista_potencias_2 = [2 ** n for n in range(1, 11)]

# o una lista de los multiplos de 5 impares menores a 100

lista_multiplos_5 = [5 * k for k in range(10) if k % 2 == 1]


# compresión de diccionarios
# sirve para crear un diccionario similar a como pasa con las listas
# por ejemplo, un diccionario que contenga palabras como llaves y su longitud como valor

dict_palabras_len = {palabra: len(palabra) for palabra in ("hola", "soy", "programador")}


# compresión de generadores
# crea un generador que puede producir una secuencia que puede ser evaluada por ciclos for

gen = (i + 2 for i in range(50))
