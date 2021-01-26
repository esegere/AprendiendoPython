# los módulos son la forma en que podemos organizar el código para evitar la repetición
# los módulos son piezas de código que tienen funcionalidad en común
# python tiene diferentes módulos incluidos en su librería standard, con ellos podemos ahorrarnos escribir código
# usando las funciones y clases de estos módulos podemos simplificar y extender el alcance de nuestros programas
#
# para usar código de un módulo es necesario "importar" dicha funcionalidad
#
# las sintaxis para importar módulos son:
#
# import NOMBRE_MODULO
import collections
# from MODULO import FUNCTION1, FUNCTION2, ...
from sys import argv, path
# como agregado se puede poner un alias a las funciones y clases importadas
# util para acortar nombres y evitar nombres iguales
import operator as op
# también es útil al importar una sola función
from functools import reduce as red

# con esta sintaxis importamos el módulo entero y para usar una clase o función dentro de el
# debemos usar NOMBRE_MODULO.NOMBRE_FUNCTION
imported_simply = collections.deque()

# de esta forma podemos importar varias clases y funciones al mismo tiempo
imported_multiple1 = argv[0]
imported_multiple2 = path

# se puede conservar el orden pero acortar los nombres
op.eq(1, 2)

# y asi usar un nombre personalizado para usar el original en otro lado
reduce = red(
    op.add,
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
)
