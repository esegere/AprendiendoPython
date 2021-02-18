# para poder realizar aplicaciones mas ricas
# el manejo de archivos es importante ya que es nuestra
# primera forma de almacenamiento permanente
# en ellos podemos escribir pero también podemos leer
# almacenar datos en ellos y después cargarlos en el programa

# para poder operar con archivos, python tiene funcionalidades
# la principal de ellas es la función open()
# que nos permite especificar un archivo para abrirlo y operarlo

# esta función recibe 2 parámetros, el nombre del archivo y el modo de apertura
# ambos como cadenas de texto

arc_lectura = open("prueba-archivos.txt", "r")
arc_escritura = open("prueba-archivos.txt", "w")
arc_escritura_al_final = open("prueba-archivos.txt", "a")
arc_lectura_y_escritura = open("prueba-archivos.txt", "r+")

# esta función devuelve un objeto con el que se puede operar el archivo
# este objeto tiene diferentes métodos para poder moverse, leer, escribir
# así como realizar algunas validaciones

# read() lee el contenido de un archivo y lo introduce en una cadena de texto
contenido = arc_lectura_y_escritura.read()

# readlines() lee el archivo e introduce cada linea de texto en un elemento de una lista
contenido_lineas = arc_lectura_y_escritura.readlines()

# readline() lee solo una linea del archivo y devuelve esa linea en una cadena
contenido_linea = arc_lectura_y_escritura.readline()

# close() al final de nuestras operaciones siempre se debe cerrar el archivo con este método
# asi evitamos errores y liberamos recursos
arc_lectura_y_escritura.close()

# seek() posiciona al archivo en el n-esimo carácter
arc_lectura_y_escritura.seek(5)

# tell() regresa la posición actual del cursor de lectura y/o escritura
arc_lectura_y_escritura.tell()

# write(string) escribe el texto dentro de la posición actual
arc_lectura_y_escritura.write("texto")

# writelines() escribe una lista de cadenas, una cadena en cada linea
arc_lectura_y_escritura.writelines(["lineas", "separadas", "en", "una", "lista"])
