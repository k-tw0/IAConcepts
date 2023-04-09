import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# cargamos los datos
data = pd.read_csv("datos.csv")

# seleccionamos las características y la variable objetivo
X = data[["habitaciones", "tamaño_lote", "ubicacion"]]
y = data["precio"]

# creamos un objeto de regresión lineal y ajustamos el modelo
reg = LinearRegression().fit(X, y)

# hacemos una predicción para una casa con 3 habitaciones, 1000 pies cuadrados de terreno y ubicada en una buena ubicación
x_new = np.array([3, 1000, 1]).reshape(1, -1)
prediccion = reg.predict(x_new)

print(f"El precio estimado de la casa es: ${prediccion[0]:,.2f}")