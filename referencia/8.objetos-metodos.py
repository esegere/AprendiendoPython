# las clases ademas de atributos tienen métodos
# los métodos son funciones que están ligadas a los datos de la clase y/o el objeto
# los métodos se definen igual que las funciones, solo hay dos condiciones
# 1.- deben estar declarados dentro  de una clase
# 2.- su primer parámetro debe ser 'self'
# los métodos pueden tener mas parámetros, pero estos vendrán después de 'self'
# los métodos pueden regresar datos o no

class ExampleClass:

    # este es un método especial
    # llamado automáticamente después de la creación de un objeto para inicializar sus atributos
    def __init__(self):
        self.attribute1 = "nombre del objeto"
        self.attribute2 = 3
        self.attribute3 = {}
        not_an_attribute = 6.1
        self.attribute4 = not_an_attribute + 5

    # método con datos de retorno
    def list_attributes(self):
        return self.attribute1, self.attribute2, self.attribute3, self.attribute4

    # método con argumentos
    def increment_all_numbers(self, amount):
        self.attribute2 += amount
        self.attribute4 += amount


# para llamar un método se instancia un objeto primero
# después se pueden llamar los métodos definidos usando el '.'
new_object = ExampleClass()
tuple_of_attributes = new_object.list_attributes()
# si el método fue declarado con algún argumento, se debe pasar este también en la llamada
new_object.increment_all_numbers(5)
