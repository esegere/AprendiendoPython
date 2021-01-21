# se pide codificar un programa que administre una agenda telefonica
# los datos que se almacenan en la agenda son:
#   1. nombre del contacto
#   2. número de teléfono
#
# la agenda debe mostrar las siguientes opciones de operación dentro de un ciclo
#   1) consultar número de contacto
#   2) agregar contacto
#   3) eliminar contacto
#   4) modificar número de contacto
#   5) salir
#
# en caso de seleccionar una opción inexistente en los menús
# notificar al usuario con el mensaje "opción no valida"
#
# al seleccionar una opción validas harán la acción correspondiente dentro de las siguientes
#   1) pedir al usuario que ingrese el nombre del contacto que busca
#           - si el contacto existe, mostrar "el numero de {PERSONA} es {NUMERO}"
#           - si el contacto no existe, mostrar "{PERSONA} no esta registrado en tu agenda"
#
#   2) pedir el nombre del contacto, después el numero del contacto y almacenar estos datos
#
#   3) pedir al usuario el nombre del contacto que desea eliminar
#           - si el contacto existe, eliminarlo y mostrar mensaje "{PERSONA} fue eliminado"
#           - si el contacto no existe, mostrar "{PERSONA} no esta registrado en tu agenda"
#
#   4) pedir al usuario el nombre del contacto que desea modificar
#           - si el usuario esta registrado, pedir al usuario el nuevo numero de teléfono
#               registrar el nuevo numero en vez del anterior y mostrar
#               "numero de {PERSONA} ha sido cambiado de {NUMERO_ANTERIOR} a {NUEVO_NUMERO}"
#           - si el contacto no existe, mostrar "{PERSONA} no esta registrado en tu agenda"
#
#   5) romper el ciclo para salir de la aplicación
#
#   PISTA: como es costumbre mia, la colección predilecta para este ejercicio es el diccionario
#   NOTA: para que las funciones puedan usar el diccionario de la agenda, pasarlo por parámetro
#   PETICIÓN: para facilitar la estructura del código crear funciones, no hay limite, el criterio es suyo

MENU = '''
    OPCIONES:
        1) Consultar número de contacto
        2) Agregar contacto
        3) Eliminar contacto
        4) Modificar número de contacto
        5) Salir
'''

agenda_telefonica = {}


def buscar_contacto(agenda_telefonica):
    contacto = input("Nombre: ").capitalize()
    if contacto in agenda_telefonica.keys():
        numero = agenda_telefonica[contacto]
        print(f'\nEl numero de {contacto} es {numero}.')
    else:
        mensaje_error(contacto)


def pedir_datos(agenda_telefonica):
    nombre = input("Nombre: ").capitalize()
    numero = input("Numero: ")
    agenda_telefonica[nombre] = numero


def eliminar_contacto(agenda_telefonica):
    nombre = input("Nombre: ").capitalize()
    if nombre in agenda_telefonica.keys():
        del agenda_telefonica[nombre]
        print(f'\n{nombre} fue eliminada')
    else:
        mensaje_error(nombre)


def modificar_contacto(agenda_telef2onica):
    nombre = input("Nombre: ").capitalize()
    if nombre in agenda_telefonica.keys():
        numero_aterior = agenda_telefonica[nombre]
        numero_nuevo = input("Nuevo numero: ")
        agenda_telefonica[nombre] = numero_nuevo
        print(f"\nnumero de {nombre} ha sido cambiado de {numero_aterior} a {numero_nuevo}")
    else:
        mensaje_error(nombre)


def mensaje_error(nombre_contacto):
    print(f"\n{nombre_contacto} no esta registrada en tu agenda")


def imprimir_error():
    print("\nOpcion no valida")


if __name__ == '__main__':
    while True:
        print(MENU)
        opcion = input("Opcion: ")
        if opcion == "1":
            buscar_contacto(agenda_telefonica)
        elif opcion == "2":
            pedir_datos(agenda_telefonica)
        elif opcion == "3":
            eliminar_contacto(agenda_telefonica)
        elif opcion == "4":
            modificar_contacto(agenda_telefonica)
        elif opcion == "5":
            break
        else:
            imprimir_error()
