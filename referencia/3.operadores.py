# operadores aritméticos
# producen un resultado relacionado a los operandos

# suma
addition_int = 1 + 5
addition_float = 1.2 + 5.8
addition_string = "dos cadenas" + "concatenadas"  # al sumar cadenas, se concatena su contenido

# resta
subtraction_int = 4 - 2
subtraction_float = 6.2 - 1.7

# multiplicación
times_int = 4 * 2
times_float = 5 * 4.5
times_string = "cadena" * 3  # se puede multiplicar una cadena por un entero de esta forma para repetir la cadena

# división
divided_int = 4 / 2  # la division SIEMPRE produce un 'float'
divided_float = 5.5 / 2.1

# division entera, esta es una division con redondeo al entero mas cercano
floor_divided_int = 4 // 2
floor_divided_float = 5.5 // 2.1  # la division entera siempre produce un 'int'

# modulo, entrega el residuo de una division entera
remainder_int = 5 % 2

# potenciación
power_int = 2 ** 8
power_float = 2.5 ** 4


# operadores de asignación
# operan sobre los valores de la derecha e izquierda y asignan el resultado a la variable de la izquierda
int_var = 2
float_var = 5.5
string_var = "cadena"

# suma
int_var += 2
float_var += 5.8
string_var += "otra cadena"  # concatena la cadena nueva dentro de la variable anterior

# resta
int_var -= 1
float_var -= 2.1

# multiplicación
int_var *= 2
float_var *= 5.5
string_var *= 3  # copia el contenido de la cadena y lo repite n veces, luego lo asigna a la misma variable

# division
int_var /= 2
float_var /= 5.1

# division entera
int_var //= 1
float_var //= 3.4

# modulo
int_var %= 5

# potenciación
int_var **= 2
float_var **= 2.3

# operadores de comparación
# comparan el valor de dos datos, siempre regresan un valor tipo bool
# los operadores son <, > ,<=, >=, == y !=
# estos funcionan como lo esperamos en números, en cadenas comparan su orden alfabético
comp = 4 == 6
comp3 = 2.1 > 3.5
comp2 = "aaa" >= "aab"
comp4 = 4 != 6
comp6 = 2.1 < 3.5
comp5 = "aaa" <= "aab"

# operadores lógicos
# operan sobre datos tipo bool y también retornan un valor tipo bool
# los operadores son and, or y not
bool_value1 = True and False
bool_value2 = True or False
bool_value3 = not True

# operador de pertenencia
# verifica la existencia de un dato dentro de una colección (normalmente listas o tuplas), devuelve un valor tipo bool

bool_value4 = 1 in (1, 2, 3, 4, 5, 6)
bool_value5 = 7 in (1, 2, 3, 4, 5, 6)

# operador de identidad (is, is not)
tuple1 = (1, "cadena")
tuple2 = tuple1
tuple3 = (1, "cadena")
# verifica si dos variables contienen el mismo objeto

bool_value6 = tuple1 is tuple2
bool_value7 = tuple1 is not tuple2
pass
