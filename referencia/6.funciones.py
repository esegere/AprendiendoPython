# las funciones son bloques de código que se pueden reutilizar, se definen una vez y se pueden reusar 
# cada función comienza con la palabra 'def' seguida del nombre , después los argumentos entre paréntesis
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


def main():
    saludar_a_todos()
    saludar_a("jessy")


# es común crear la función main solo por organización
if __name__ == '__main__':
    main()
