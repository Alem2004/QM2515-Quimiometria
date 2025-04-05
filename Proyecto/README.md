# Red Neuronal para Predicción de Concentraciones

Este proyecto utiliza una red neuronal para predecir la concentración de una muestra a partir de datos de absorbancia obtenidos mediante espectroscopía UV-Visible. El modelo se entrena con datos de calibración y realiza predicciones sobre una muestra desconocida.

## Archivos

- **`red_neuronal.py`**: Script principal que implementa el modelo de red neuronal.
- **`Datos-UV-Visible.xlsx`**: Archivo Excel que contiene los datos de calibración y de la muestra. Este archivo debe estar en el mismo directorio que el script.

## Requisitos

Antes de ejecutar el script, se deben instalar las siguientes dependencias:

- `pandas`
- `numpy`
- `scikit-learn`
- `tensorflow`

## Funcionamiento del Script

### 1. **Lectura de Datos**
- Se lee el archivo `Datos-UV-Visible.xlsx`.
- Se cargan dos hojas:
  - `UV- de calibracion`: Contiene datos de absorbancia y concentraciones conocidas.
  - `UV- muestra`: Contiene datos de absorbancia de la muestra a predecir.

### 2. **Procesamiento de Datos**
- **Datos de Calibración**:
  - Se extraen las absorbancias y concentraciones de las columnas correspondientes.
  - Las columnas de absorbancia se rellenan con ceros para igualar su longitud.
- **Datos de la Muestra**:
  - Se ajustan las dimensiones de los datos de la muestra para que coincidan con los datos de calibración.

### 3. **Preprocesamiento**
- Se utiliza `StandardScaler` para escalar los datos de calibración y de la muestra, normalizando los valores para mejorar el rendimiento del modelo.

### 4. **Definición de la Red Neuronal**
- La red neuronal tiene la siguiente arquitectura:
  - Capa densa con 64 neuronas y activación ReLU.
  - Capa de Dropout con una tasa de 0.1.
  - Capa densa con 32 neuronas y activación ReLU.
  - Capa de salida con 1 neurona y activación lineal.
- Se compila el modelo utilizando el optimizador `adam` y la función de pérdida `mse` (error cuadrático medio).

### 5. **Entrenamiento**
- El modelo se entrena con los datos de calibración.
- Se utiliza `EarlyStopping` para detener el entrenamiento si la pérdida no mejora después de 10 épocas consecutivas.

### 6. **Predicción**
- Una vez entrenado, el modelo realiza una predicción sobre los datos de la muestra.
- La concentración predicha se imprime en la consola.

## Ejecución

Para ejecutar el script:

```bash
python red_neuronal.py
```

El archivo `Datos-UV-Visible.xlsx` debe estar en el mismo directorio o sino se debe ajustar la ruta en el script.

## Salida

El script imprimirá en la consola:
- La forma de los datos de calibración y de la muestra antes y después del ajuste.
- La arquitectura del modelo de red neuronal.
- La concentración predicha para la muestra en partes por millón (ppm).

## Notas

- Si el archivo `Datos-UV-Visible.xlsx` no se encuentra, el script mostrará un mensaje de error y se detendrá.
- Asegúrate de que las hojas del archivo Excel tengan los nombres correctos (`UV- de calibracion` y `UV- muestra`).
- El modelo está diseñado para trabajar con un número específico de tablas de calibración (7 en este caso). Si el archivo tiene un formato diferente, será necesario ajustar el código.