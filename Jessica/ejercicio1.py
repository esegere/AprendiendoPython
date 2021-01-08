def main():
# crear una variable de cada tipo e imprimir su valor
    #booleanos
    verdad = True
    mentira = False

    #Entero positivo y negativo
    inicio_amor = 100
    limite_de_amor = -100
    cantidad = 1_000_000_000_000_000_000

    #cosas raras que ya se me olvidaron
    bin = 0b11
    octal = 0o11
    hexad = 0x11

    #flotantes
    flotante = 54.5
    notacion_cientifica = 54e-20

    #string
    mensaje = f'''Hola bebe, Te amo. Tengo un mensaje para ti
    Nunca dudes que te amo porque siempre sera {verdad}
    En ningun momento de nuestras vidas el resultado sera {mentira}
    la cantidad en la que puedes medir mi amor es mayor a este numero: {cantidad}
    '''

    print(mensaje)


if __name__ == "__main__":
    main()
