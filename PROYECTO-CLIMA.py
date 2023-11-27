# Importar bibliotecas
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Supongamos que tenemos un conjunto de datos históricos con fechas y temperaturas
# Estos datos deberían ser recopilados de la plantación de aguacates
data = {'Fecha': [1, 2, 3, 4, 5, 6],
        'Temperatura': [25, 28, 24, 30, 32, 29]}
df = pd.DataFrame(data)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(df[['Fecha']], df['Temperatura'], test_size=0.2, random_state=42)

# Crear y entrenar el modelo de regresión lineal
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Interacción con el usuario para ingresar fechas
try:
    fecha_7 = float(input("Ingrese la fecha para la predicción (por ejemplo, 7): "))
    fecha_8 = float(input("Ingrese otra fecha para la predicción (por ejemplo, 8): "))
except ValueError:
    print("Error: Ingrese valores numéricos para las fechas.")
    exit()

# Predecir temperaturas para las fechas ingresadas por el usuario
nuevas_fechas = pd.DataFrame({'Fecha': [fecha_7, fecha_8]})
predicciones = modelo.predict(nuevas_fechas)

# Imprimir las predicciones
for fecha, prediccion in zip(nuevas_fechas['Fecha'], predicciones):
    print(f"Predicción de temperatura para la fecha {fecha}: {prediccion:.2f} °C")

# Graficar el modelo y las predicciones
plt.scatter(df['Fecha'], df['Temperatura'], color='black', label='Datos reales')
plt.plot(df['Fecha'], modelo.predict(df[['Fecha']]), color='blue', linewidth=3, label='Modelo de regresión lineal')
plt.scatter(nuevas_fechas['Fecha'], predicciones, color='red', label='Predicciones para nuevas fechas')
plt.xlabel('Fecha')
plt.ylabel('Temperatura (°C)')
plt.title('Predicción de Temperaturas para Cultivo de Aguacates')
plt.legend()
plt.show()
