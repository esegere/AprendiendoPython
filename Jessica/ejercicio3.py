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
    ALTO = "Alto"
    print(MENSAJE_REGISTRO)
    # código para registrar candidatos en esta sección
    nombre = None
    dic_candidatos = {}
    while nombre != ALTO:
        nombre = input("Canditado: ").capitalize().strip(" ")
        if nombre != ALTO and nombre != "":
            dic_candidatos[nombre] = 0
    # fin de registro de candidatos

    print(MENSAJE_VOTACION)
    # código para votar en esta sección
    for nom_candidatos in dic_candidatos:
        print(f'\t - {nom_candidatos}')
    voto = None
    print("\n")
    while voto != ALTO:
        voto = input("Candidato: ").capitalize().strip(" ")
        if voto in dic_candidatos.keys():
            dic_candidatos[voto] += 1
        elif voto == ALTO:
            break
        else:
            print("Candidato no registrado")
    # fin de votación
    print(MENSAJE_CONTEO)
    # código para conteo en esta sección
    can_ganador = None
    sort_dic = list(dic_candidatos.values())
    sort_dic.sort()
    max_votos = sort_dic[len(sort_dic) - 1]
    for rec_candidatos in dic_candidatos.keys():
        if max_votos == dic_candidatos[rec_candidatos]:
            can_ganador = rec_candidatos
    print(f'El ganador es: {can_ganador} con {max_votos} votos.')
    # fin de conteo

# yeii, bien hecho, te amo mi vida hermosa
