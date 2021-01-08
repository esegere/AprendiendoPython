#  Python es un lenguaje orientado a objetos
#  y como tal se pueden construir objetos a partir de clases y también se pueden escribir clases

# las clases se escriben iniciando con la palabra reservada 'class' seguida del nombre de la clase

class ExampleClass:
    # podemos definir atributos estáticos o de clase aquí
    # estos NO son los atributos de las instancias
    static_attribute1 = 0
    static_attribute2 = "nombre de clase"
    static_attribute3 = []

    # este método especial es donde podemos definir e inicializar las variables del objeto
    # este método siempre tiene un argumento llamado 'self', que representa al objeto actual
    def __init__(self):
        # para declarar atributos del objeto se antepone 'self.' de otra forma solo sera una variable local
        self.attribute1 = "nombre del objeto"
        self.attribute2 = 3
        self.attribute3 = {}
        # este no es un atributo, solo una variable
        not_an_attribute = 6.1
        # pero la variable se puede usar para inicializar otros atributos
        self.attribute4 = not_an_attribute + 5


# para crear un objeto de la clase que acabamos de crear
# se invoca el constructor de la clase
# simplemente se escribe el nombre de la clase seguido de paréntesis
# esto producirá un nuevo objeto que puede ser asignado a una variable

new_object = ExampleClass()
