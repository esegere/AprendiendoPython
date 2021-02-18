# na de las aplicaciones mas comunes de las funciones de alto orden
# son los decoradores, estos son funciones de alto orden que modifican o extienden una función
# así como sintaxis para poder utilizarlos
#
# un decorador es una función de alto orden quq acepta una función y devuelve otra función
# se definen de esta forma

def decorador(func):
    def envoltura(*args):  # para poder redirigir todos los argumentos
        # funcionalidad extra
        print("decorado")
        return func(*args)  # aquí se llama la función original

    return envoltura  # se devuelve la función interna, sin paréntesis


# y esta lista para aplicarse a cualquier función
# este decorador agregara un print como funcionalidad extra
#
# para usar un decorador
# es usa @nombre_del_decorador sobre la definición de una función

@decorador  # asi se decora una función
def imprimir_mensaje_2_veces(mensaje):  # la función conserva su propósito, pero adquiere funcionalidad
    print(f"{mensaje} {mensaje}")


if __name__ == '__main__':
    # la sintaxis de "@" del decorador es equivalente a hacer
    # imprimir_mensaje_2_veces = decorador(imprimir_mensaje_2_veces)
    imprimir_mensaje_2_veces("hola")
