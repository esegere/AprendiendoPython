# en python tenemos las estructuras condicionales

condition = True
condition2 = False

# if
# si la condición evaluada es verdadera, el código dentro del bloque se ejecuta

if condition:
    print("la condición es verdadera")

# if-else
# si la condición evaluada es verdadera, el código dentro del bloque 'if' se ejecuta
# de ser falsa, se ejecuta el código dentro del bloque 'else'

if condition:
    print("la condición es verdadera")
else:
    print("la condición es falsa")

# if-elif-else
# si la condición evaluada es verdadera, el código dentro del bloque 'if' se ejecuta
# cada 'elif' contiene una condición diferente e la del 'if', estas se evalúan solo si no se cumple el 'if'
# se pueden poner N cantidad de 'elif', en cuanto alguno de ellos se cumpla, se ejecuta su bloque de código
# por ultimo si ninguna condición se cumplió se ejecuta el código dentro del 'else'

if condition and condition2:
    print("las condiciones son verdaderas")
elif condition and not condition2:
    print("solo la condición 1 es verdadera")
elif not condition and condition2:
    print("solo la condición 2 es verdadera")
else:
    print("ninguna condición es verdadera")

# operador ternario
# una forma de asignar valores a una variable de acuerdo a una condición
# variable = valor1 if condición else valor2
# la estructura evalúa la condición primero
# si la condición es verdadera la variable se iguala al valor de la izquierda (valor1)
# si la condición es falsa la variable se iguala al valor de la derecha (valor2)

variable = "primer valor" if condition else "segundo valor"
print(variable)
