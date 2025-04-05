import math

def calcular_moles(masa, masa_molar):
    """Calcula el número de moles dado una masa y la masa molar."""
    moles = masa/masa_molar
    return moles

def calcular_PH(concentracion_h):
    """Calcula el pH de una solución dada la concentración de iones H+."""
    if concentracion_h <= 0:
        raise ValueError("La concentración de iones H+ debe ser mayor que cero.")
    pH = -math.log10(concentracion_h)
    return pH

def calcular_concentracion(moles, volumen):
    """Calcula la concentración en mol/L."""
    if volumen <= 0:
        raise ValueError("El volumen debe ser mayor que cero.")
    return moles / volumen

def calcular_rendimiento_teorico(rendimiento_real, rendimiento_teorico):
    """Calcula el rendimiento porcentual de una reacción."""
    if rendimiento_teorico <= 0:
        raise ValueError("El rendimiento teórico debe ser mayor que cero.")
    return (rendimiento_real / rendimiento_teorico) * 100

def calcular_PH2(ka, acido, base):
    """Calcula el pH de una solución tampón a partir de la concentración de un ácido débil y su base conjugada."""
    if acido <= 0 or base <= 0 or ka <= 0:
        raise ValueError("Las concentraciones y Ka deben ser mayores que cero.")
    pka = -math.log10(ka)
    return pka + math.log10(base / acido)

def predecir_solubilidad(kps, concentracion_ionica):
    """Predice si un compuesto será soluble o insoluble en solución."""
    if kps <= 0 or concentracion_ionica <= 0:
        raise ValueError("El Kps y la concentración iónica deben ser mayores que cero.")
    return "El compuesto es insoluble." if concentracion_ionica > kps else "El compuesto es soluble."