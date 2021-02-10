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


DATOS_DE_ALUMNOS = """"
   1.-Agregar alumno
   2.-Consultar promedio grupal
   3.-Consultar promedio de cada uno
   4.-Consultar cuantos alumnos son de excelencia
   5.-Salir
"""


class Alumno:

    def __init__(self, nombre, calificacion_1er_parcial, calificacion_2do_parcial, calificacion_3er_parcial):
        self.Nombre = nombre
        self.Calificacion_1er_parcial = calificacion_1er_parcial
        self.Calificcion_2do_parcial = calificacion_2do_parcial
        self.Calificacion_3er_parcial = calificacion_3er_parcial


    def get_nombre(self):
        return self.Nombre


    def calificacion_total(self):
        calificacion = self.Calificacion_1er_parcial + self.Calificcion_2do_parcial + self.Calificacion_3er_parcial
        promedio = calificacion / 3
        return promedio


    def calificacion_excelencia(self):
        if self.calificacion_total() > 7.9:
            return True
        else:
            return False


lista_agregar_alumno = []


def Agregar_alumno(list_datos_de_alumnos):
    nombre_alumno = input("Nombre:")
    calificacion1 = float(input("Ingrese sus calificacion 1er parcial:"))
    calificacion2 = float(input("Ingrese su calificacion del 2do parcial:"))
    calificacion3 = float(input("Ingrese su calificacion del 3er parcial:"))

    alumno = Alumno(nombre_alumno, calificacion1, calificacion2, calificacion3)
    lista_agregar_alumno.append(alumno)


def Calcular_calificaciones_grupal(list_datos_alumnos):
    total = 0
    for alumno in list_datos_alumnos:
        total += alumno.calificacion_total()
    promedio_grupal = total / len(list_datos_alumnos)
    print(f"El promedio grupal es de {promedio_grupal}:")


def Consultar_promedio_individual(list_datos_alumnos):
    for alumno in list_datos_alumnos:
        print(f"nombre del alumno:{alumno.Nombre},el promedio del alumno:{alumno.calificacion_total()}")


def Consultar_alumnos_excelencia(list_datos_alumnos):
    for alumno in list_datos_alumnos:
        print(f"nombre del alumno:{alumno.Nombre},¿tiene excelencia?{alumno.calificacion_excelencia()}")


def imprimir_error():
    print("Opcion no Valida")


if __name__ == '__main__':

    while True:
        print(DATOS_DE_ALUMNOS)
        option = input("opciones del menu")
        if option == "1":
            print(f"Agregar alumno: ")
            Agregar_alumno(lista_agregar_alumno)
        elif option == "2":
            print(f"Consultar promedio grupal: {Calcular_calificaciones_grupal(lista_agregar_alumno)}")
        elif option == "3":
            print(f"Consultar promedio de cada uno :")
            Consultar_promedio_individual(lista_agregar_alumno)
        elif option == "4":
            print(f"Consultar cuantos alumnos son de exelencia: ")
            Consultar_alumnos_excelencia(lista_agregar_alumno)
        elif option == "5":
            break
        else:
            imprimir_error()
