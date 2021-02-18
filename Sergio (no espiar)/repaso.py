# 4 tipos de datos
_string = "string"  # jessy
_int = 5  # xochitl
_float = 5.8
_bool = True or False

# 3 colecciones principales
diccionario = {"llave": "valor"}  # jessy
lista = ["el1", "el2", "el3"]  # xochitl     se el pueden insertar, borrar o modificar elementos
tupla = ("asf", 5)  # jessy    a esta no


# declarar funciones con parámetros y valores de retorno
def funcion(parametro):
    return parametro * 2


# declarar funciones sin argumentos
def funcion_s():
    print("print")


# declarar una clase con su constructor
class Clase:
    def __init__(self):
        self.atributo = 5

    def get_nombre(self):
        return "mi nombre"


if __name__ == '__main__':
    funcion(5)
    objeto = Clase()
    valor_5 = objeto.atributo  # el operador punto, accede a los métodos o atributos de un objeto
    nombre = objeto.get_nombre()  # método, se llama igual que llamar a una función
