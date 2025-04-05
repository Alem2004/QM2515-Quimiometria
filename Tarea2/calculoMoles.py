def calcular_moles(masa, masa_molar):
    """
    Calcula el número de moles dado una masa y la masa molar.
    
    Parámetros:
    masa (float): La masa de la sustancia en gramos.
    masa_molar (float): La masa molar de la sustancia en gramos por mol.
    
    Retorna:
    float: El número de moles de la sustancia.
    """
    
    moles = masa/masa_molar
    return moles

masa = float(input("Introduce la masa del compuesto (en gramos): "))
masa_molar = float(input("Introduce la masa molar del compuesto (en g/mol): "))

# Calcular los moles
moles = calcular_moles(masa, masa_molar)

# Mostrar el resultado
print(f"Los moles del compuesto son: {moles}")
