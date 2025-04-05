import numpy as np
import matplotlib.pyplot as plt

# Datos del problema
T0 = 300  # Temperatura inicial del pastel (°F)
Tm = 70   # Temperatura ambiente (°F)
T_3min = 200  # Temperatura despues de 3 minutos (°F)
t_dado = 3  # Tiempo dado en minutos


# Despejamos la ecuacion: T(t) = Tm + (T0 - Tm) * exp(kt)
# T(t) - Tm = (T0 - Tm) * exp(kt)
# ln(T(t) - Tm) = ln(T0 -Tm) + kt
# kt = ln((T(t) - Tm) / (T0 - Tm))

# Resolver para k para cuando T(t) = 200
k = np.log((T_3min - Tm) / (T0 - Tm)) / t_dado

# Resolver para t cuando T(t) = 75°F, ligeramente por encima de Tm para evitar un log(0)
t_objetivo = 72
t_final = np.log((t_objetivo - Tm) / (T0 - Tm)) / k

print(f"Constante de enfriamiento k = {k:.4f}")
print(f"Tiempo para alcanzar 70°F = {t_final:.2f} minutos")

# Generar datos para la grafica
t_values = np.linspace(0, t_final + 5, 100)
T_values = Tm + (T0 - Tm) * np.exp(k * t_values)

# Graficar la curva de enfriamiento
plt.figure(figsize=(8, 5))
plt.plot(t_values, T_values, label="Temperatura del pastel", color='b')
plt.axhline(y=70, color='r', linestyle='--', label="70°F (Meta)")
plt.axvline(x=t_final, color='g', linestyle='--', label=f"Tiempo estimado: {t_final:.2f} min")
plt.xlabel("Tiempo (min)")
plt.ylabel("Temperatura (°F)")
plt.title("Enfriamiento del Pastel (Ley de Newton)")
plt.legend()
plt.grid()
plt.show()