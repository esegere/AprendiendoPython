# para dar mejor soporte al paradigma funcional
# tenemos un tipo de función especial llamada lambda
# este concepto se pede encontrar en otros lenguajes que soporten programación funcional
# también es les conoce como funciones literales
#
# estas expresiones crean funciones sin nombre
# especialmente útiles cuando se necesita una función como parámetro
# ya que permiten definir una función ahi mismo
# sin tener que preocuparnos por que solo se use en esa función o método en especial

# la sintaxis de una lambda es :
#                   lambda parámetros: operación
# lambda x, y: x + y  # regresa la suma de 2 números


# las lambdas regresan el valor de la operación que se les asigna

# supongamos se tiene una función que acepta una lista y una función
# esta regresará una nueva lista con todos los elementos resultantes de aplicar
# la función a los elementos de la lista original

def mapear(lista, funcion):  # esta función es muy común
    return [funcion(elemento) for elemento in lista]


# tenemos una lista con los números del 1 al 10

numeros_nomales = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# y queremos usar la función mapear para tener una lista con el doble de cada numero
# como necesitamos pasar una función
# debemos definir une función que multiplique por 2 un numero

def duplicar(numero):
    return numero * 2


# acabamos de definir una función que solo usaremos una vez y cuyo cuerpo es muy sencillo

if __name__ == '__main__':
    numeros_duplicados = mapear(numeros_nomales, duplicar)
    # pero podemos usar una lambda para realizar la operación sin definir ninguna función fuera
    numeros_duplicados2 = mapear(numeros_duplicados, lambda num: num * 2)
    # haciendo el código mas corto y conveniente
