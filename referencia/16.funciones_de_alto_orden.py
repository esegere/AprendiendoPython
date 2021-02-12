# ya observamos el poder de las funciones
# sin embargo eso no es lo único que tienen por ofrecernos
#
# python también soporta el paradigma de programación funcional
# este paradigma se centra en las funciones para transformar datos de entrada en datos de salida
# y una de las características mas versátiles son las funciones de alto orden
#
# estas son funciones que aceptan otras funciones como parámetros, o regresan funciones desde ellas
#
# son útiles para extender algunas funciones predefinidas
# o construir nuevas de forma dinámica

def multiples_veces(f, *args):
    for arg in args:
        f(arg)


# para poder regresar funciones desde dentro de una función, podemos definir funciones anidadas
# esta última tiene acceso a todas las variables de la función que la contiene, pero también puede recibir parámetros
# y definir sus propias variables, esta solo tendrá nombre dentro de la función contenedora
# fuera de esta, el nombre no existirá

def decir_(palabra):  # esta función genera mas funciones que dirán lo que necesitemos
    def interna(nombre):
        print(f"{palabra} {nombre}")  # hacemos uso de variables internas y de la función contenedora

    return interna  # la función interna se regresa sin los paréntesis
    # de otra forma se estaría llamando a la función y regresando su resultado
    # pero deseamos retornar la función no su resultado


# después podemos usar pocas funciones para hacer mucho mas
if __name__ == '__main__':
    decir_hola = decir_("hola")  # las funciones también se pueden asignar a variables y guardar en colecciones
    multiples_veces(decir_hola, "Horacio", "Gonzalo", "Daniel")
    print()
    lista_saludos = [decir_(saludo) for saludo in
                     (
                         "hola",
                         "buenos dias",
                         "buenas tardes",
                         "como estas?"
                     )]
    nombres = (
        "Fernando",
        "Ramon",
        "Saul",
        "Antonio",
        "Gustavo"
    )
    for saludo in lista_saludos:
        multiples_veces(saludo, *nombres)
