import numpy as np
import matplotlib.pyplot as plt


# EDO
def f(t, y):
    return y * t**2 - 1.1 * y

# Solucion analitica
def solucion_analitica(t):
    C = 1  # y(0) = 1
    return C * np.exp((t**3 / 3) - 1.1 * t)

# Método de Euler
def euler(f, y0, t0, tf, h):
    t_values = np.arange(t0, tf + h, h)
    y_values = np.zeros(len(t_values))
    y_values[0] = y0
    
    for i in range(1, len(t_values)):
        y_values[i] = y_values[i-1] + h * f(t_values[i-1], y_values[i-1])
    
    return t_values, y_values

# Método de Runge-Kutta de cuarto orden
def rk_4(f, y0, t0, tf, h):
    t_values = np.arange(t0, tf + h, h)
    y_values = np.zeros(len(t_values))
    y_values[0] = y0
    
    for i in range(1, len(t_values)):
        t = t_values[i-1]
        y = y_values[i-1]
        
        k1 = h * f(t, y)
        k2 = h * f(t + h/2, y + k1/2)
        k3 = h * f(t + h/2, y + k2/2)
        k4 = h * f(t + h, y + k3)
        
        y_values[i] = y + (k1 + 2*k2 + 2*k3 + k4) / 6
    
    return t_values, y_values

# Definimos el intervalo y condicion inicial
t0, tf = 0, 2
y0 = 1

# Solucion analitica
t_exact = np.linspace(t0, tf, 100)
y_exact = solucion_analitica(t_exact)

# Solucion metodo de Euler
t_euler_1, y_euler_1 = euler(f, y0, t0, tf, 0.5)
t_euler_2, y_euler_2 = euler(f, y0, t0, tf, 0.25)

# Solucion metodo RK de cuarto orden
t_rk, y_rk = rk_4(f, y0, t0, tf, 0.5)

# Graficar resultados
plt.figure(figsize=(8,6))
plt.plot(t_exact, y_exact, 'k-', label='Solución Analítica')
plt.plot(t_euler_1, y_euler_1, 'r--', label='Euler h=0.5')
plt.plot(t_euler_2, y_euler_2, 'g--', label='Euler h=0.25')
plt.plot(t_rk, y_rk, 'b-.', label='Runge-Kutta h=0.5')
plt.xlabel('t')
plt.ylabel('y')
plt.title('Comparación de Métodos Numéricos')
plt.legend()
plt.grid()
plt.show()