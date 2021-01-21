# existen métodos especiales que se comportan y se pueden llamar de forma distinta
# todos los métodos que caen en esta categoría tienen una característica en común
# todos empiezan y terminen con "__" (doble guion bajo)
#
# un ejemplo de esta categoría es el método "constructor" __init__
#
# la mayoría de estos métodos están relacionados a un operador
class ExampleClass:

    # método constructor de la clase
    def __init__(self):
        self.numero = 8

    # los métodos especiales tienen definida la cantidad de parámetros que deben de aceptar
    # al intentar definirlos el IDE nos ayuda a auto completar correctamente

    # método que se llama al usar el operador  +
    def __add__(self, other):
        return self.numero + other

    # método que se llama al usar el operador  -
    def __sub__(self, other):
        return self.numero - other

    # método que se llama al usar el operador  *
    def __mul__(self, other):
        return self.numero * other

    # método que se llama al usar el operador  /
    def __truediv__(self, other):
        return self.numero / other

    # método que se llama al usar el operador  ==
    def __eq__(self, other):
        return self.numero == other

    # método que se llama al usar el operador  >
    def __gt__(self, other):
        return self.numero > other

    # método que se llama al usar el operador  >=
    def __ge__(self, other):
        return self.numero >= other

    # método que se llama al convertir el dato en un string (esto lo hace la función print)
    def __str__(self):
        return f"mi numero es: {self.numero}"

    # y muchos mas, uno para cada operador y también palabras claves


if __name__ == '__main__':
    obj = ExampleClass()
    var = obj + 2
    print(var)
    print(obj)
