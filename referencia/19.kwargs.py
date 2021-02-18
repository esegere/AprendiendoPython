# en python, además de  poder pasar una cantidad variable de parámetros normales
# podemos pasar una cantidad variable de parámetros con nombre
# a este conjunto de argumentos pasados por nombre se les conoce como:
#       kwargs
#       keyword arguments
# para recibir este tipo de argumentos en nuestras funciones y métodos
# debemos de declarar un argumento precedido de "**" dos asteriscos

# este parámetro almacenará los argumentos en un diccionario que puede ser usado dentro de la función
def funcion(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


if __name__ == '__main__':
    funcion(saludo="hola", nombre="José", edad=52)
