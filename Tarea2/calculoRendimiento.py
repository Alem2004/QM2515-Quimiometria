def calcular_rendimiento_teorico(rendimiento_real, rendimiento_teorico):
    """
    Calcula el rendimiento porcentual de una reaccion quimica.
    
    Parametros: 
    rendimiento_real: Cantidad de producto obtenido (gramos o moles)
    rendimiento_teorico: Cantidad de producto esperado teoricamente (gramos o moles)
    
    Retorna:
    Rendimiento porcentual
    """
    if rendimiento_teorico <= 0:
        raise ValueError("El rendimiento teorico debe ser mayor que cero.")
    return (rendimiento_real / rendimiento_teorico) * 100

rendimiento_real = float(input("Introduce el rendimiento real de la reacción (en gramos): "))
rendimiento_teorico = float(input("Introduce el rendimiento real de la reacción (en gramos): "))

# Calcular el rendimiento
rendimiento = calcular_rendimiento_teorico(rendimiento_real, rendimiento_teorico)

# Mostrar el resultado
print(f"El rendimiento teorico de la reaccion es: {rendimiento}")