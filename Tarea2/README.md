# Aprendiendo Python!

Este directorio contiene varios scripts en Python que implementan funciones relacionadas con cálculos químicos y matemáticos en funcion de aprender el funcionamiento. A continuación, se describen los archivos y las funciones principales que contienen:

## Archivos y Funciones

### 1. `calculoConcentracion.py`
- Calcula la concentración de un compuesto en moles por litro. Recibe como parametros la cantidad de moles del compuesto y volumen de la solucion en litros.


### 2. `calculoMoles.py`
- Calcula el numero de moles dado una masa y la masa molar. Recibe como parametros la masa de la sustancia en gramos y la masa molar de la sustancia en g/mol.

### 3. `calculoPH.py`
- Calcula el ph de una solucion dada la concentracion de iones H+. Recibe la concentracion de iones H+ en moles por litro.

### 4. `calculoPH2.py`
- Calcula el pH de una solución tampón a partir de la concentración de un ácido débil y su base conjugada. Recibe como parametros constante de acidez del acido debil, la concentración del ácido débil (mol/L) y concentración de la base conjugado.

### 5. `calculoRendimiento.py`
- Calcula el rendimiento porcentual de una reacción química. Recibe como parametros cantidad de producto obtenido (gramos o moles) y cantidad de producto esperado teóricamente (gramos o moles).

### 6. `predecirSolubilidad.py`
- Predice si un compuesto será soluble o insoluble en solución. Recibe como parametros el producto de solubilidad (Kps) y el producto de las concentraciones ionicas de una solucion.

### 7. `quimica_utilidades.py`
- Modulo que contiene las funciones implementadas en todos los archivos antes mencionados. Las funciones son:
  - `calcular_moles(masa, masa_molar)`
  - `calcular_PH(concentracion_h)`
  - `calcular_concentracion(moles, volumen)`
  - `calcular_rendimiento_teorico(rendimiento_real, rendimiento_teorico)`
  - `calcular_PH2(ka, acido, base)`
  - `predecir_solubilidad(kps, concentracion_ionica)`

### 8. `sen_cos_aprox.py` y `sen_cos_igual.py`
- Ambas funciones aproximan el seno y el coseno de un determinado angulo a partir de su serie de Taylor, el archivo `sen_cos_aprox_py` compara la aproximacion con la funcion seno y  coseno de la libreria `math`, mientras que `sen_cos_igual.py` verifica cuando el coseno y el seno son iguales.

## Uso
Cada archivo puede ejecutarse de forma independiente. Al ejecutarlos, se solicitarán al usuario los datos necesarios para realizar los cálculos y se mostrarán los resultados en la salida estandar.

## Requisitos
- Librerías estándar de Python (`math`)