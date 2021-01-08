# las funciones son bloques de código que se pueden reutilizar, se definen una vez y se pueden reusar 
# cada función comienza con la palabra 'def' seguida del nombre
# después los argumentos entre paréntesis separados por coma
# luego el código a ejecutar
# dentro s puede incluir una sentencia 'return' opcional
# esta sentencia terminara la función y devolverá el valor a quien llamo la función  
# una función debe ser definida antes de ser usada

def crear_saludo(nombre):
    return f"hola {nombre}"


def saludar_a(nombre):
    print(crear_saludo(nombre))


def saludar_a_todos():
    saludar_a("a todos")


# al anteponer un asterisco (*) al nombre de un parámetro
# podemos encapsular en esa variable todos los argumentos que sean pasados a la función
# este parámetro que encapsula muchos datos debe ser siempre el ultimo de todos
def saludar_a_varios(*nombres):
    print("saludando a varias personas:")
    # este parámetro se trata como una tupla, por lo tanto se puede usar un ciclo 'for' con el
    for nombre in nombres:
        saludar_a(nombre)


# asi mismo podemos tener varios valores de retorno
# separándolos por una coma
def separar_nombre(nombre_completo):
    nombre_dividido = nombre_completo.split()
    return nombre_dividido[0], nombre_dividido[1]


# dentro de los parámetros se pueden especificar valores por defecto
# para asignar un valor por defect, solo se escribe el nombre del parámetro, seguido de un '=' y el valor por defecto
# estos valores serán asignados a las variables si el usuario no proporciona valores diferentes
def imprimir_por_partes(nombre_completo, incluir_nombre=True, incluir_apellido=True):
    # se puede obtener los valores por separado cuando una función devuelve varios datos
    # poniendo los datos separados por una coma del lado izquierdo de la igualdad
    nombre, apellido = separar_nombre(nombre_completo)
    mensaje = ""
    if incluir_nombre:
        mensaje += f" nombre: {nombre}"
    if incluir_apellido:
        mensaje += f" apellido: {apellido}"
    print(mensaje)


# es común crear la función main solo por organización
def main():
    saludar_a_todos()
    saludar_a("jessy")
    saludar_a_varios("Jessy", "Xóchitl", "Sergio")
    imprimir_por_partes("Jessica Rodriguez")  # esta llamada usa los valores por defecto que declaramos
    imprimir_por_partes("Xóchitl Miranda", False)  # esta llamad solo usa el ultimo valor por defecto
    # en caso de querer especificar un valor solo para un parámetro especifico
    # y mantener los demás con los valores por defecto
    # se puede especificar el nombre del parámetro seguido de un '=' y el valor
    # estos parámetros deben pasarse al final de la llamada
    imprimir_por_partes("Sergio Garcia", incluir_apellido=False)  # ademas sirve como auto-documentación


# y usar este bloque de código para llamar a la función main solo si es desde este archivo
if __name__ == '__main__':
    main()
