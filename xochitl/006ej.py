# se pide crear un programa para llevar los datos de los alumnos de un profesor
# cada alumno tiene la información:
#   1. nombre
#   2. calificación  1er parcial
#   3. calificación  2do parcial
#   4. calificación  3er parcial
# las operaciones que el profesor podrá hacer son:
#   1. agregar alumno
#   2. consultar promedio grupal
#   3. consultar promedio de cada alumno
#   4. consultar cuantos alumnos son de excelencia (promedio mayor a 7.9)
#   5. salir
# se debe mostrar un menú con las opciones anteriores y pedir que se seleccione una
# al ingresar una opción se debe hacer la función seleccionada, si la opción no existe
# imprimir el mensaje "opción no valida"
#
# 1) para agregar un alumno se debe pedir su nombre y cada una de sus calificaciones
#
# 2) se debe calcular el promedio grupal de todas las evaluaciones parciales
#
# 3) se debe calcular el promedio de cada alumno con sus 3 calificaciones y mostrar una lista con el formato:
#       alumno: promedio
#
#
# crear una clase alumno que contenga nombre y las 3 calificaciones
# esta clase debe tener:
#   - un método constructor
#   - una propiedad "promedio" que calcule el promedio de sus 3 calificaciones
#   - un método tiene_excelencia()  para saber si el alumno es de excelencia
#
# guardar los alumnos en una lista
