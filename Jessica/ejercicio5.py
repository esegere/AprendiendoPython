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
