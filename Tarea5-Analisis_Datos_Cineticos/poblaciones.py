import numpy as np
import matplotlib.pyplot as plt

def modelo_competencia(x, y):
    """
    Define el sistema de ecuaciones diferenciales:
    dx/dt = x(1 - 0.1x - 0.05y)
    dy/dt = y(1.7 - 0.15x - 0.1y)
    """
    dxdt = x * (1.0 - 0.1*x - 0.05*y)
    dydt = y * (1.7 - 0.15*x - 0.1*y)
    return dxdt, dydt

def rk_4(f, x0, y0, t0, tf, h):
    """
    Metodo Runge-Kutta de orden 4 para un sistema de 
    dos ecuaciones diferenciales.
    
    Args:
        f: Función que devuelve las derivadas (dxdt, dydt)
        x0, y0: Condiciones iniciales
        t0, tf: Tiempo inicial y final
        h: Paso de tiempo
    
    Returns:
        t, x, y: Arrays con los valores de tiempo y soluciones
    """
    # Inicializar arreglos de soluciones
    num_pasos = int((tf - t0)/h) + 1
    t = np.linspace(t0, tf, num_pasos)
    x = np.zeros(num_pasos)
    y = np.zeros(num_pasos)
    
    # Condiciones iniciales
    x[0] = x0
    y[0] = y0
    
    # Iteracion con RK4
    for i in range(num_pasos - 1):
        # Paso 1
        k1_x, k1_y = f(x[i], y[i])
        
        # Paso 2
        k2_x, k2_y = f(x[i] + 0.5*h*k1_x, y[i] + 0.5*h*k1_y)
        
        # Paso 3
        k3_x, k3_y = f(x[i] + 0.5*h*k2_x, y[i] + 0.5*h*k2_y)
        
        # Paso 4
        k4_x, k4_y = f(x[i] + h*k3_x, y[i] + h*k3_y)
        
        # Actualizamos valores
        x[i+1] = x[i] + (h/6)*(k1_x + 2*k2_x + 2*k3_x + k4_x)
        y[i+1] = y[i] + (h/6)*(k1_y + 2*k2_y + 2*k3_y + k4_y)
    
    return t, x, y

# Definimos los parametros de simulación
t0 = 0
tf = 50  # años
h = 0.01  # paso de tiempo

# Diccionario con los casos a estudiar
casos = {
    'Caso a': {'x0': 1.1, 'y0': 1, 'label': 'Caso a) x(0) = 1.1, y(0) = 1'},
    'Caso b': {'x0': 4, 'y0': 10, 'label': 'Caso b) x(0) = 4, y(0) = 10'}
}

# Configurar gráficos
plt.figure(figsize=(10, 6))

# Resolver y graficar para cada caso
for nombre, caso in casos.items():
    
    label = caso['label']
    t, x, y = rk_4(modelo_competencia, caso['x0'], caso['y0'], t0, tf, h)
    
    # Grafico de evolucion temporal
    plt.plot(t, x, label=f'{label} -> x(t)')
    plt.plot(t, y, '--', label=f'{label} -> y(t)')
    

# Configuracion de graficos
plt.title('Evolución de las Poblaciones en el Tiempo (RK4)')
plt.xlabel('Tiempo (años)')
plt.ylabel('Población (miles)')
plt.grid(True)
plt.legend()
plt.show()
