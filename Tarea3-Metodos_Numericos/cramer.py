import numpy as np

def cramer(A, B):
    det_A = np.linalg.det(A)  # Determinante de la matriz A
    if np.isclose(det_A, 0):
        raise ValueError("El sistema no tiene solución única (determinante es cero)")
    
    n = A.shape[0]
    solutions = []
    
    for i in range(n):
        Ai = A.copy()
        Ai[:, i] = B  # Reemplaza la columna i con el vector B
        det_Ai = np.linalg.det(Ai)  # Determinante de Ai
        solutions.append(det_Ai / det_A)
    
    return solutions

# Definir la matriz de coeficientes A y el vector B
A = np.array(
            [[0.3, 0.52, 1],
            [0.5, 1, 1.9],
            [0.1, 0.3, 0.5]]
            )

B = np.array([-0.01, 0.67, -0.44])

# Resolver usando la Regla de Cramer
soluciones = cramer(A, B)
print("La solucion al sistema de ecuaciones es:")
# Imprimir soluciones
for i, x in enumerate(soluciones, start=1):
    print(f"x{i} = {x:.4f}")