def predecir_solubilidad(kps, concentracion_ionica):
    """
    Predice si un compuesto sera soluble o insoluble en solucion.
    
    Parametros:
    kps: Producto de solubilidad (Kps)
    concentracion_ionica: Producto de las concentraciones ionicas en solucion
    
    Retorna:
    True: si el compuesto es soluble
    False: si el compuesto es insoluble
    """
    if kps <= 0 or concentracion_ionica <= 0:
        raise ValueError("El Kps y la concentracion ionica deben ser mayores que cero.")
    
    if concentracion_ionica > kps:
        return False # Es insoluble
    else:
        return True # Es soluble


concentracion_ionica = float(input("Introduce la concentracion (en moles/litro): "))
kps = float(input("Introduce el valor del Kps del compuesto: "))

solubilidad = predecir_solubilidad(kps, concentracion_ionica)

if solubilidad:
    print("El compuesto es soluble en solucion")
else:
    print("El compuesto es insoluble")