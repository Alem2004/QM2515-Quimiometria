def factorial(n):
    """
    Calcula el factorial de un número dado.   

    Parametros:
    n (int): El número del cual se desea calcular el factorial. Debe ser un entero no negativo.

    Retorna:
    int: El factorial del número dado.
    """
    
    # Caso base
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1) # Caso n - 1

def seno(x, terminos=10):
    """
    Calcula la aproximación del seno de un ángulo en radianes utilizando la serie de Taylor.

    Parámetros:
    x (float): El ángulo en radianes del cual se desea calcular el seno.
    terminos (int, opcional): El número de términos de la serie de Taylor a utilizar para la aproximación. Por defecto es 10.

    Retorna:
    float: La aproximación del seno del ángulo dado.
    """
    sen_x = 0
    for n in range(terminos):
        coeficiente = (-1) ** n
        numerador = x ** (2 * n + 1)
        denominador = factorial(2 * n + 1)
        sen_x += coeficiente * (numerador / denominador)
    return sen_x

def coseno(x, terminos=10):
    """
    Calcula la aproximación del coseno de un ángulo en radianes utilizando la serie de Taylor.

    Parámetros:
    x (float): El ángulo en radianes del cual se desea calcular el coseno.
    terminos (int, opcional): El número de términos de la serie de Taylor a utilizar para la aproximación. Por defecto es 10.

    Retorna:
    float: La aproximación del coseno del ángulo dado.
    """
    cos_x = 0
    for n in range(terminos):
        coeficiente = (-1) ** n
        numerador = x ** (2 * n)
        denominador = factorial(2 * n)
        cos_x += coeficiente * (numerador / denominador)
    return cos_x

# Pruebas para comparar con el modulo math
def main():
    import math

    # Pedimos la entrada al usuario
    angulo = float(input("Ingrese el ángulo en radianes: "))
    
    # Calculamos el seno y el coseno del angulo mediante la aproximacion
    seno_aprox = seno(angulo)
    coseno_aprox = coseno(angulo)
    
    # Calculamos el seno y el coseno del angulo mediante el modulo math
    seno_math = math.sin(angulo)
    coseno_math = math.cos(angulo)
    
    # Imprimimos resultados
    print(f"Seno aproximado: {seno_aprox}, Seno modulo math: {seno_math}")
    print(f"Coseno aproximado: {coseno_aprox}, Coseno modulo math: {coseno_math}")


if __name__ == "__main__":
    main()