# la herencia es parte fundamental de la programación orientada a objetos
# pues con esto podemos lograr reutilizar código de una forma muy simple
#
class Base:

    def __init__(self):
        self.atributo1 = 0
        self.atributo2 = ""

    def hacer_algo(self):
        print(f"haciendo algo {self.atributo1} veces con {self.atributo2}")


# para que una clase herede de otra se debe poner el nombre de la clase padre dentro de paréntesis
# justo delante del nombre de la nueva clase
# se pueden usar mas de una clase como clase padre

class Derived(Base):

    def __init__(self):
        # podemos llamar explícitamente al constructor del padre
        super().__init__()
        self.atributo1 = 300
        self.atributo3 = []

    def hacer_otra_cosa(self):
        print(f"haciendo otra cosa {self.atributo1} veces, sin nadie")


# asi se logra heredar las funcionalidades que anteriormente fueron implementadas para las clases padre

# El polimorfismo es el otro de los 3 pilares de la  programación orientada a objetos
# esta característica nos permite usar un objeto de un tipo, como si fuera de otro tipo
# asi solo nos interesamos únicamente en las características del objeto que nos importan
# el polimorfismo en Python es tan simple como usar el método, o atributo de una clase sin importar de que tipo sea
# mientras lo tenga podremos llamarlo

class OtraClase:

    def hacer_algo(self):
        print("haciendo algo en otro lado")


def hacerle_algo_al_objeto(objeto):
    objeto.hacer_algo()


if __name__ == '__main__':
    objeto1 = Base()
    objeto2 = Derived()
    objeto3 = OtraClase()
    hacerle_algo_al_objeto(objeto1)
    hacerle_algo_al_objeto(objeto2)
    hacerle_algo_al_objeto(objeto3)

    # objeto1.hacer_algo()
    # objeto2.hacer_algo()
