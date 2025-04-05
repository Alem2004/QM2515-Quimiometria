
def calcular_concentracion(moles, volumen):
    """
    Calcula la concentracion de un compuesto en moles por litro (mol/L).
    
    Parametros:
    moles (float): Cantidad de moles del compuesto
    volumen (float): Volumen de la solucion en litros
    
    
    float: Concentracion en mol/L
    """
    if volumen <= 0:
        raise ValueError("El volumen debe ser mayor que cero.")
    return moles / volumen


moles = float(input("Introduce la cantidad de moles del compuesto: "))
volumen = float(input("Introduce el volumen de la solucion (en litros): "))

# Calcular la concentracion
concentracion = calcular_concentracion(moles, volumen)

# Mostrar el resultado
print(f"La concentracion del compuesto es: {concentracion} (mol/L)")