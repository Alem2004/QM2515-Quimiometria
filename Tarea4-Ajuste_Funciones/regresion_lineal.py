import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Datos del problema
x = np.array([1, 2, 3, 5, 5])
y = np.array([0.5, 2, 2.9, 3.5, 4])

# Aplicamos una transformacion logaritmica.
ln_x = np.log(x)

# Aplicamos regresion lineal
slope, intercept, r_value, p_value, std_err = linregress(ln_x, y)


# Calculamos los parametros
a = 1 / slope
b = -intercept * a

print(f"Parámetros obtenidos: a = {a:.4f}, b = {b:.4f}")

# Prediccion para x = 2.6
x_pred = 2.6
y_pred = intercept + slope * np.log(x_pred)
print(f"Predicción para x = 2.6: y = {y_pred:.4f}")

# Graficamos los datos y la regresion
plt.scatter(ln_x, y, color='red', label='Datos')
plt.plot(ln_x, intercept + slope * ln_x, label='Regresión lineal', color='blue')
plt.xlabel('ln(x)')
plt.ylabel('y')
plt.title('Regresión lineal de datos transformados')
plt.legend()
plt.grid()
plt.show()  