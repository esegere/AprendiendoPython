# tenemos varios tipos de datos básicos en python
# todos estos datos son clases, pero no tenemos que importar nada para usarlos
# además el tipo de las variables es dinámico, lo que significa que no tenemos que declarar su tipo
# una vez que se asigna un valor a una variable, esta lleva el tipo de la variable que se le asignó

# bool
# este tipo de dato solo tiene 2 posibles valores True y False

bool_true = True
bool_false = False

# int
# este tipo contiene números enteros, se pueden manejar números muy grandes, no hay limite para la capacidad
# se puede asignar valores positivos o negativos
# como extra se puede separar as cifras con un '_' para facilidad de lectura sin afectar al valor
# también se pueden asignar valores binarios, octales o hexadecimales anteponiendo un '0b', '0o' o '0x' respectivamente

int_positive = 16
int_negative = -35
int_big = 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000
int_bin = 0b10  # 2
int_octal = 0o10  # 8
int_hex = 0x10  # 16

# float
# este tipo contiene números con punto decimal
# estos números se pueden escribir con notación científica también

float_normal = 8.56
float_scientific = 8e-20

# strings
# este tipo de dato contiene cadenas de texto
# en python no hay diferenciación entre un carácter y una cadena de texto
# la cadena de texto puede estar entre un par de comillas simples(') o comillas dobles(")
# adicionalmente se pueden usar triples comillas (simples o dobles)
# y asi ocupar mas de una linea(conservando saltos de linea en la cadena)
# las cadenas con comillas simples pueden contener comillas dobles como carácter de la cadena y viceversa

string_simple = 'cadena con comillas simples'
string_double = "cadena con comillas dobles"
string_simple_double = 'cadena con comillas simples y "comillas dobles" dentro'
string_double_simple = "cadena con comillas dobles y 'comillas simples' dentro"
string_triple_simple = '''
cadena con comillas triples simples
que ocupa varias lineas
'''
string_triple_double = """
cadena con comillas triples dobles
que ocupa varias lineas
"""

# un tipo especial de string son las f-strings
# se identifican por ser como cualquier tipo de cadena anterior pero con una 'f' antes
# estas permiten interpolar valores de variables dentro de la cadena
# es decir, copiar el valor de la variable adentro de una cadena
# para especificar la variable a interpolar, esta se pone dentro de un par de llaves '{}'

string_f = f'''cadena f-string
puede interpolar
bool: {bool_true}
int: {int_negative}
float: {float_scientific}
otras strings: {string_simple}
y mas...
'''
print(string_f)
