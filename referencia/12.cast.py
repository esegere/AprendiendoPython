# a pesar de que no tenemos tipos estáticos en python
# esto no significa que no tengamos tipos
# hay cosas que ciertos tipos son capaces de hacer y otros no
# cuando se presenta el caso en el que requerimos transformar a un tipo de dato en otro
# es cuando ocupamos una característica del lenguaje llamada cast
#
# este consiste en intentar transformer un dato hacia un tipo diferente al actual
#
# para realizar esta operación basta con hacer una llamada a una función especial
# con el nombre del tipo al que se desea convertir, como si de un constructor de una clase se tratara

entero_en_cadena = "549"
flotante_en_cadena = "945.85"
tupla = ( "tupla", "de", "palabras")

# conversiones

entero_desde_cadena = int(entero_en_cadena)
flotante_desde_cadena = float(flotante_en_cadena)
lista_desde_tupla = list(tupla)
numero_en_cadena = str(5489.21)
tupla_desde_lista = tuple(lista_desde_tupla)

# no todas las conversiones son posibles en todos los casos
# por eso hay que asegurarnos de manejar las excepciones correspondientes
