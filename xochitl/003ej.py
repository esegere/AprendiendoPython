# se pide crear un sistema para registrar candidatos para unas elecciones
# asi como registrar y contabilizar los votos que la gente hace por los candidatos
# y después determinar al ganador
#
# codificar el programa que simule el registro de candidatos, las votaciones y muestre el candidato electo
#
# a) el programa debe pedir desde la linea de comandos el nombre de los candidatos a registrar de uno en uno
#   después de haber registrado a todos los candidatos se debe escribir "alto"
#   entonces se termina el registro y empieza con la votación
#
# b) el programa debe mostrar los nombres de los candidatos por los cales se puede votar
#   y pedir que el usuario vote por algún candidato de uno por uno, para terminar la votación se escribe "alto"
#   en caso de introducir el nombre de un candidato no registrado mostrar el mensaje "candidato no registrado"
#   y descartar el voto
#
# c) al terminar las votaciones el programa debera anunciar al candidato ganador (el que tenga mas votos)
#   asi como su numero de votos
#   de la siguiente forma "el ganador es: NOMBRE con VOTOS votos"
#
# NOTA: no modificar ninguna parte del código existente, solo agregar las funcionalidades

MENSAJE_REGISTRO = """
                  .----------.
                  | REGISTRO |
                  '----------'
Ingrese los nombres de los candidatos uno por uno

"""

MENSAJE_VOTACION = """
                  .----------.
                  | VOTACIÓN |
                  '----------'
Ingrese el nombre del candidato votado uno por uno

"""

MENSAJE_CONTEO = """
                    .--------.
                    | CONTEO |
                    '--------'
Fin de la votación los resultados del conteo son...

"""

if __name__ == '__main__':

    print(MENSAJE_REGISTRO)
    # código para registrar candidatos en esta sección
    dic_registro = {}
    nombre = None
    while nombre != "alto":
        nombre = input("Ingrese un candidato: ")
        dic_registro[nombre] = 0

    print(MENSAJE_VOTACION)
    # código para votar en esta sección
    print(dic_registro.keys())
    votacion = None
    while votacion !="alto":
        votacion=input("Ingrese su votacion: ")
        if votacion in dic_registro.keys():
            dic_registro[votacion] += 1
        else:
            print("Candidato no registrado")



    # fin de votación

    condicion_1= "registro de candidatos"
    condicion_2= "resgistro de votos "

    print(MENSAJE_CONTEO)

    dic_registro.values()
    max_votos=0

    for candidato_evaluado in dic_registro.values():
        if  candidato_evaluado >= max_votos:
            max_votos = candidato_evaluado

    nombre_ganador=""
    for candidato_ganador  in dic_registro.keys():
        if dic_registro[candidato_ganador] == max_votos:
            nombre_ganador= candidato_ganador

    print(f"EL GANADOR ES : {nombre_ganador} CON {max_votos}" )



    # código para conteo en esta sección

    # fin de conteo
