import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Datos experimentales
t = np.array([0, 100, 200, 300, 400, 600, 1000])  # tiempo en segundos
A_A0 = np.array([1, 0.829, 0.688, 0.597, 0.511, 0.385, 0.248])  # [A]/[A]₀
A0 = 0.600  # mol/dm³
A = A_A0 * A0  # Concentración real [A]

# Funciones para diferentes órdenes de reacción
def orden_cero(t, A, A0):
    """Análisis para reacción de orden cero"""
    # Gráfico de A vs t
    slope, intercept, r_value, _, _ = linregress(t, A)
    plt.figure(figsize=(12, 4))
    plt.subplot(131)
    plt.plot(t, A, 'o', label='Datos')
    plt.plot(t, intercept + slope*t, 'r-', label=f'Ajuste (r²={r_value**2:.4f})')
    plt.xlabel('t (s)')
    plt.ylabel('[A] (mol/dm³)')
    plt.title('Orden cero: [A] vs t')
    plt.legend()
    plt.grid(True)
    return slope, r_value**2

def orden_uno(t, A, A0):
    """Análisis para reacción de primer orden"""
    # Gráfico de ln(A) vs t
    ln_A = np.log(A)
    slope, intercept, r_value, _, _ = linregress(t, ln_A)
    plt.subplot(132)
    plt.plot(t, ln_A, 'o', label='Datos')
    plt.plot(t, intercept + slope*t, 'r-', label=f'Ajuste (r²={r_value**2:.4f})')
    plt.xlabel('t (s)')
    plt.ylabel('ln[A]')
    plt.title('Primer orden: ln[A] vs t')
    plt.legend()
    plt.grid(True)
    return -slope, r_value**2

def orden_dos(t, A, A0):
    """Análisis para reacción de segundo orden"""
    # Gráfico de 1/A vs t
    inv_A = 1/A
    slope, intercept, r_value, _, _ = linregress(t, inv_A)
    plt.subplot(133)
    plt.plot(t, inv_A, 'o', label='Datos')
    plt.plot(t, intercept + slope*t, 'r-', label=f'Ajuste (r²={r_value**2:.4f})')
    plt.xlabel('t (s)')
    plt.ylabel('1/[A] (dm³/mol)')
    plt.title('Segundo orden: 1/[A] vs t')
    plt.legend()
    plt.grid(True)
    return slope, r_value**2

# Realizar los tres ajustes
k0, r2_0 = orden_cero(t, A, A0)
k1, r2_1 = orden_uno(t, A, A0)
k2, r2_2 = orden_dos(t, A, A0)

plt.tight_layout()
plt.show()

# Determinar el mejor ajuste (mayor coeficiente de determinación R²)
ordenes = {
    'Cero': r2_0,
    'Uno': r2_1,
    'Dos': r2_2
}

mejor_orden = max(ordenes, key=ordenes.get)
mejor_r2 = ordenes[mejor_orden]

# Resultados
print("\nResultados del análisis:")
print(f"1) Orden de la reacción: {mejor_orden} (R² = {mejor_r2:.4f})")

if mejor_orden == 'Cero':
    print(f"2) Constante de velocidad (k): {k0:.4f} mol dm⁻³ s⁻¹")
elif mejor_orden == 'Uno':
    print(f"2) Constante de velocidad (k): {k1:.4f} s⁻¹")
else:
    print(f"2) Constante de velocidad (k): {k2:.4f} dm³ mol⁻¹ s⁻¹")

print("\nCoeficientes de determinación (R²):")
print(f"- Orden cero: {r2_0:.4f}")
print(f"- Primer orden: {r2_1:.4f}")
print(f"- Segundo orden: {r2_2:.4f}")