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
ALTO = "Alto"

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
    candidatos = {}
    while True:
        nuevo_nombre = input("nombre del candidato: ").capitalize().strip(" ")
        if nuevo_nombre == ALTO:
            break
        candidatos[nuevo_nombre] = 0
    # fin de registro de candidatos
    print(MENSAJE_VOTACION)
    # código para votar en esta sección
    for nombre in candidatos.keys():
        print(nombre)
    while True:
        voto = input("por quien desea votar?: ").capitalize().strip(" ")
        if voto == ALTO:
            break
        if voto in candidatos.keys():
            candidatos[voto] += 1
        else:
            print("candidato no registrado")
    # fin de votación
    print(MENSAJE_CONTEO)
    # código para conteo en esta sección
    ganador, votos = next(
        (key, value) for key, value in candidatos.items() if value == max(candidatos.values())
    )
    print(f"el ganador es {ganador} con {votos} votos")
    # fin de conteo
