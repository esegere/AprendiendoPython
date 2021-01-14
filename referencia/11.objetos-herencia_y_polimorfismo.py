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

class Derived(Base):

    def __init__(self):
        # podemos llamar explícitamente al constructor del padre
        super().__init__()
        self.atributo1 = 300
        self.atributo3 = []

    def hacer_otra_cosa(self):
        print(f"haciendo otra cosa {self.atributo1} veces, sin nadie")
