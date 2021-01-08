# tenemos estructuras para repetir código conocidas como ciclos
number = 5
list_numbers = [45, 51, 87, 72, 18, 62, 5, 38, 21, 19]
# while
# esta estructura repite n bloque de código mientras se cumpla la condición evaluada

while number > 0:
    print('se cumple')
    number -= 1

# for
# esta estructura repite el código del bloque una vez or cada elemento de una colección
# al mismo tiempo, los elementos se van evaluando uno a uno y se pueden usar dentro del bloque de código

for number in list_numbers:
    print(number)

# para conseguir el funcionamiento clasico de un 'for' en otros lenguajes
# se usa una función especial llamada range
# esta función recibe de 1 a 3 parámetros

# un parámetro indica que se quiere recorrer de uno en uno los números del 0 al numero anterior al parámetro
var1 = range(12)  # 0,1 2,3,4,5,6,7,8,9,10,11

# dos parámetros indican que se iniciara desde el primer parámetro, avanzando de uno en uno hasta el número
# anterior al segundo parámetro
var2 = range(4, 10)  # 4,5,6,7,8,9

# tres parámetros indican que se iniciara desde el primero, avanzando el numero del tercer parámetro
# hasta el numero anterior al segundo parámetro dentro de la serie

var3 = range(2, 12, 2)  # 2,4,6,8,10

# el 'for' indexado se escribe entonces asi

for i in range(number):
    print(list_numbers[i])
pass
