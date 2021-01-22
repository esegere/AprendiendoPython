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


class Alumno:
    def __init__(self,
                 nombre_alumno,
                 calificacion_primer_parcial,
                 calificacion_segundo_parcial,
                 calificacion_tercer_parcial):
        self._nombre_alumno = nombre_alumno
        self.calificacion_primer_parcial = calificacion_primer_parcial
        self.calificacion_segundo_parcial = calificacion_segundo_parcial
        self.calificacion_tercer_parcial = calificacion_tercer_parcial

    @property
    def nombre_alumno(self):
        return self._nombre_alumno

    @property
    def promedio(self):
        resultado = (self.calificacion_primer_parcial
                     + self.calificacion_segundo_parcial
                     + self.calificacion_tercer_parcial) / 3
        return resultado

    def tiene_excelencia(self):
        if self.promedio > 7.9:
            return True
        else:
            return False


MENU = '''
    OPCIONES:
        1. Agregar alumno
        2. Consultar promedio grupal
        3. Consultar promedio de cada alumno
        4. Consulta de excelencia
        5. Salir
'''
lista_de_alumnos = []


def agregar_alumno(lista_de_alumnos):
    nombre_alumno = input("\nNombre del Alumno: ")
    calificacion_primer_parcial = float(input("Calificacion del primer parcial: "))
    calificacion_segundo_parcial = float(input("Calificacion del segundo parcial: "))
    calificacion_tercer_parcial = float(input("Calificacion del tercer parcial: "))
    nuevo_alumno = Alumno(nombre_alumno,
                          calificacion_primer_parcial,
                          calificacion_segundo_parcial,
                          calificacion_tercer_parcial)
    lista_de_alumnos.append(nuevo_alumno)


def calcular_promedio_grupal(lista_de_alumnos):
    promedios = 0
    for alumno in lista_de_alumnos:
        promedios += alumno.promedio
    return promedios / len(lista_de_alumnos)


def consultar_promedios(lista_de_alumnos):
    for datos in lista_de_alumnos:
        print(f'\nNombre: {datos.nombre_alumno} Promedio: {datos.promedio:.2f}')


def consultar_excelencia(lista_de_alumnos):
    excelencia = 0
    for alumno in lista_de_alumnos:
        if alumno.tiene_excelencia():
            excelencia += 1
    return excelencia


def imprimir_error():
    print("\nOpcion no valida")


if __name__ == '__main__':
    while True:
        print(MENU)
        opcion = input("Opcion: ")
        if opcion == "1":
            agregar_alumno(lista_de_alumnos)
        elif opcion == "2":
            print(f"\nPromedio general del grupo: {calcular_promedio_grupal(lista_de_alumnos):.2f}")
        elif opcion == "3":
            consultar_promedios(lista_de_alumnos)
        elif opcion == "4":
            print(f'\nLa cantidad de alumnos con excelencia es: {consultar_excelencia(lista_de_alumnos)}')
        elif opcion == "5":
            break
        else:
            imprimir_error()
