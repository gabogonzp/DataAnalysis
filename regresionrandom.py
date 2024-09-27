
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import  r2_score, mean_squared_error

#Carga de datos
data = pd.read_csv('wine-quality.csv')

#Características
x = data.drop('quality', axis=1)

#Objetivo de regresión
y = data['quality']

#División del conjunto en datos de entrenamiento y prueba
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state=0)

#Definición del tipo de modelo
model = RandomForestRegressor(n_estimators=100, random_state=42)

#Introducción de datos de entrenamiento al modelo
model.fit(x_train, y_train)

#Aplicación del modelo al eje de prueba para definir un resultado de regresión
y_pred = model.predict(x_test)

#Pruebas de precisión
r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)


print('R2 Score:', r2)
print('Mean Squared Error:', mse)
