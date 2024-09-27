
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import  accuracy_score, recall_score, f1_score
from sklearn.metrics import classification_report

#Carga de datos
data = pd.read_csv('wine-quality.csv')


#Características
x = data.drop('quality', axis=1)
#Objetivo de regresión
y = data['quality']

#División del conjunto en datos de entrenamiento y prueba
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state=0)

#Definición del tipo de modelo
model = RandomForestClassifier(n_estimators=100, random_state=42)

#Introducción de datos de entrenamiento al modelo
model.fit(x_train, y_train)

#Aplicación del modelo al eje de prueba para definir un resultado de regresión
y_pred = model.predict(x_test)

#Pruebas de precisión
accuracy = accuracy_score(y_test, y_pred)
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')


print('Precisión:', accuracy)
print('Recall:', recall)
print('F1 Score:', f1)