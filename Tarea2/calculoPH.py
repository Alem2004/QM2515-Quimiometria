import math


def calcular_PH(concentracion_h):
    """
    Calcula el pH de una solución dada la concentracion de iones H+.

    Parámetros:
    concentracion_h (float): La concentracion de iones H+ en moles por litro (M).

    Retorna:
    float: El pH de la solucion.
    """
    if concentracion_h <= 0:
        raise ValueError("La concentracion de iones H+ debe ser mayor que cero.")
    
    pH = -math.log10(concentracion_h)
    return pH


concentracion_h = float(input("Introduce la concentracion de H+ (en moles/litro): "))

# Calcular el ph
ph = calcular_PH(concentracion_h)

# Mostrar el resultado
print(f"El ph de la solucion es: {ph}")