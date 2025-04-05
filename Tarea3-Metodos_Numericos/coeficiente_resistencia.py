import numpy as np
import matplotlib.pyplot as plt

def velocidad(c, m, g, t):
    return (m * g / c) * (1 - np.exp(- (c / m) * t))

m = 68.1  # kg
g = 9.81  # m/s²
t = 10  # s
v_objetivo = 40  # m/s

# Rango de valores para c
c_values = np.linspace(5, 20, 100)
v_values = [velocidad(c, m, g, t) for c in c_values]

# Encontrar el valor de c que más se acerca a 40 m/s
c_optimo = c_values[np.argmin(np.abs(np.array(v_values) - v_objetivo))]
print(f"El coeficiente de resistencia óptimo es aproximadamente c = {c_optimo:.3f}")

# Graficamos
plt.plot(c_values, v_values, label="Velocidad a t=10s")
plt.axhline(y=v_objetivo, color='r', linestyle='--', label="v = 40 m/s")
plt.axvline(x=c_optimo, color='g', linestyle='--', label=f"c óptimo = {c_optimo:.3f}")
plt.xlabel("Coeficiente de resistencia c")
plt.ylabel("Velocidad (m/s)")
plt.title("Determinación gráfica del coeficiente de resistencia")
plt.legend()
plt.grid()
plt.show()