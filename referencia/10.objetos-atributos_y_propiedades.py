# por defecto en python todos los atributos son públicos
# sin importar si son estáticos  o del objeto
#
# la filosofía de python no nos prohíbe acceder a estos atributos
# confía en que el programador sabe lo que hace y no lo restringe
# sin embargo, entre programadores, aveces es necesario hacer visibles nuestras intenciones
#
class ExampleClass:

    def __init__(self):
        # para hacer ver a quien lea nuestro código que un atributo no debería ser usado públicamente
        # agregamos un "_" antes de su nombre
        self._atributo_casi_privado = 0
        # para forzar un poco mas a que no se acceda a este atributo se usan "__" doble guion bajo
        self.__atributo_mas_privado = 6

    # para los atributos privados se pueden definir un getter y un setter como en otros lenguajes
    # que son métodos que manipulan esta variable
    def set_atributo_casi_privado(self, valor):
        self._atributo_casi_privado = valor

    def get_atributo_casi_privado(self):
        return self._atributo_casi_privado

    # son estos 2 métodos se puede acceder al valor de la variable y modificarlo
    # pero hacer el llamado de eta forma no resulta en código muy legible
    #
    # en cambio en python podemos ocupar las propiedades
    # estos son métodos que se llaman cuando se intenta acceder al valor de un atributo
    # y permiten escribir código mas elegante
    #
    # propiedad (getter)
    # para declarar el getter se escribe "@property" justo arriba de el método
    # el nombre del método sera el nombre de la propiedad
    @property
    def atributo_mas_privado(self):
        return self.__atributo_mas_privado

    # propiedad (setter)
    # para declarar el setter se escribe @propiedad.setter justo arriba de el método
    # el método debe llamarse exactamente igual que la propiedad
    @atributo_mas_privado.setter
    def atributo_mas_privado(self, valor):
        self.__atributo_mas_privado = valor


if __name__ == '__main__':
    new_objeto = ExampleClass()
    # print(new_objeto._atributo_casi_privado)  # aun es posible acceder a atributos con un "_"
    # pero solo estamos siendo necios
    # print(new_objeto.__atributo_mas_privado)  # pero ya no es posible acceder de esta forma a atributos con doble "_"
    # esto los hace virtualmente privados
    # y los getters y setters de propiedades se pueden llamar como cualquier atributo
    print(new_objeto.atributo_mas_privado)
    new_objeto.atributo_mas_privado = 10
