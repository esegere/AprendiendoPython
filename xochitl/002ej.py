# agregar en una lista los numeros que introdzca el usuario
# y corregir los errores que se presenten

if __name__ == '__main__':
    lista_numeros = []  # declarar una lista vacia
    while True:
        nuevo_dato = input("ingesa un numero: ")
        lista_numeros.append(nuevo_dato)  # usar el metodo adecuado para ingresar los numeros
        print(lista_numeros)
