# en python podemos acceder a colecciones de objetos sin hacer uso de ninguna librería
# estos son estructuras que contienen un grupo de datos

# lista
# una lista es un grupo ordenado de datos que normalmente son del mismo tipo
# aunque esto no es estrictamente necesario
# las listas son colecciones mutables, es decir que después de crearlas se puede modificar su contenido
# ademas se pueden repetir elementos
# las listas se denotan como una serie de datos entre corchetes [] separados por coma
# cuando solamente aparecen los corchetes sin ningún dato, es una lista vacía []

list_ints = [1, 54, 3, 12, 4, 112, 8, 13, 24, 0, 4]
list_floats = [1.2, 54.6, 12.7, 78.6, 84.1, 326.24]
# también se puede segmentar la declaración de una lisa en diferentes lineas
list_strings = [
    'cadenas',
    'dentro'
    'de',
    'una',
    'lista'
]
list_empty = []
# para acceder a los elementos de una lista se usan los corchetes []
list_ints[4] = -5
# métodos comunes
# append: añade un elemento al final de la lista
list_ints.append(2222)
# inserta un dato en la posición especificada, el primer valor es la posición y el segundo el dato
list_ints.insert(2, 890)
# remove: si el elemento indicado existe en la lista, se elimina
list_ints.remove(112)
# clear: elimina todos los elementos (vacía la lista)
list_ints.clear()
# sort: ordena la lista de forma ascendente
list_ints.sort()
# index: busca un valor dentro d ela lista y devuelve su posición, si no lo encuentra devuelve -1
list_ints.index(13)

# tupla
# las tuplas son colecciones de elementos inmutables
# una vez definidas no se puede alterar su contenido
# las tuplas se denotan con elementos separados por comas, normalmente dentro de paréntesis (), pero no son necesarios
# también se pueden extender por varias lineas al usar paréntesis

tuple_parens = ("cadena", 1, True, 2.8)
tuple_no_parens = 5, False, 'cadena', 5.9
tuple_parens_multiline = (
    True,
    "cadena",
    9,
    1.56
)
# para acceder a los elementos de la tupla también se usan los corchetes []
# pero solo para ver los datos no podemos cambiarlos
variable_sin_usar = tuple_parens[2]

# diccionario
# es una forma especial de lista no ordenada
# contiene datos de cualquier tipo, pero el indice puede ser cualquier objeto inmutable, no solo números enteros
# lo mas común es usar cadenas como llaves
# los diccionarios son pares de datos entre llaves {} separados por comas
# cada dato del par se separa por ':" el dato de la izquierda se llama llave y el de la derecha se llama valor
# el diccionario sin datos {} solamente con llaves es un diccionario vacío
# al igual que las colecciones anteriores, se puede extender por varias lineas

dictionary = {"las": 5.6, "cadenas": 2.6, "pueden": 7.56, "ser": 1.89, "llaves": 1.85}
dictionary_multiline = {
    "las": 5.6,
    "cadenas": 2.6,
    "pueden": 7.56,
    "ser": 1.89,
    "llaves": 1.85
}
# para acceder a los datos del diccionario también se usan los corchetes []
dictionary["las"] = 12.21
# métodos comunes
# clear: vacía el diccionario
dictionary.clear()
# devuelve todas las llaves del diccionario
dictionary.keys()
# devuelve todos los valores del diccionario
dictionary.values()

# para todas las colecciones se puede usar la función 'len()' y asi obtener su tamaño

print(len(dictionary))
print(len(tuple_parens))
print(len(list_ints))
