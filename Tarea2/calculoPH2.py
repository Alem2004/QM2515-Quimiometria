import math

def calcular_PH2(ka, acido, base):
    """
    Calcula el pH de una solucion tampon partir de la concentracion de un acido 
    debil y su base conjugada.
    
    Parametros: 
    ka: Constante de acidez del acido debil (Ka)
    acido: Concentracion del acido debil (mol/L)
    base: Concentracion de la base conjugada (mol/L)
    
    Retorna:
    pH de la solucion tampon
    """
    if acido <= 0 or base <= 0 or ka <= 0:
        raise ValueError("Las concentraciones y pKa deben ser mayores que cero.")
    pka = -math.log10(ka)
    ph = pka + math.log10(base / acido)
    return ph

acido = float(input("Introduce la concentracion del acido debil (en moles/litro): "))
base = float(input("Introduce la concentracion de la base conjugada (en moles/litro): "))
ka = float(input("Introduce el valor de pKa del acido debil: "))


# Calcular el ph
ph = calcular_PH2(ka, base, acido)

# Mostrar el resultado
print(f"El pH de la solucion tampon es: {ph}")