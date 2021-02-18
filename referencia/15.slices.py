# el operador de acceso [] en python es muy poderoso
# nos sirve para acceder a un elemento de cualquiera de las colecciones principales

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
numero_2 = lista[2]

# esta forma ya nos es conocida, sin embargo
# podemos acceder a los elementos con indices negativos
# al poner un numero negativo, la colección contara desde el final hacia el inicio
# en vez del inicio al final
#
# por ejemplo, para obtener el ultimo elemento de una lista

ultimo_numero = lista[-1]  # -1 es el primer elemento desde el final de la lista, es decir, el ultimo

penultimo_numero = lista[-2]  # -2 es el segundo elemento desde el final

# de esta forma podemos acceder a los ultimo elementos si tener que usar la longitud
#
#
# ademas, tenemos la posibilidad de obtener partes de la colección, a estas partes se les llama
# slices
#
# usando el ":" como separador podemos especificar un punto de inicio, de final y un paso
# con esto podemos conseguir extraer partes mas pequeñas de una colección, o seleccionar elementos que nos interesan
#
# por ejemplo: para obtener los primeros 4 elementos de una lista

primeros_4 = lista[0:4]  # obtiene los elementos de el 0 al 3, y crea uan lista nueva con ellos

siguientes_4 = lista[4:8]  # obtiene desde el elemento 4 al 7

# al agregar paso se pueden seleccionar cada ciertos elementos
#
# por ejemplo, seleccionamos uno si y uno no  dentro de los primeros 8

primeros_pares = lista[0:9:2]  # toma un elemento de cada 2 desde el 0 al 8

# si omitimos alguno de los números, pero ponemos el ":" los valores por default son:
# para el inicio        0

primeros_5 = lista[:5]  # igual a lista[0:5]

# para el final         el final de la lista

sin_primeros_2 = lista[2:]  # desde el elemento con indice 2 hasta el final

# también podemos usar valores negativos para el inicio

ultimos_4 = lista[-4:]  # igual a

# y para el paso        1

todos = lista[0::]  # igual a lista[0::1] o lista[0:]

# un ruco muy común en el que se usan slices es invertir el orden de una lista

invertida = lista[::-1]  # todos los elementos, pero iniciando desde el final
