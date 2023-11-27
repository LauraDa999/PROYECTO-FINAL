# PROYECTO-FINAL
#  "Análisis de Datos Climáticos EN CULTIVOS AGRICOLAS" - Alternativa#3
#  Equipo Code-farmers
PRESENTADO POR:
LAURA DANIELA GARCIA CHAVES Y MARIA JOSE VALLEJO RODRIGUEZ
![image](https://github.com/LauraDa999/Taller1/assets/141860731/433b1645-87dd-48eb-84d6-fc6bc19051d4)

# PRESENTACION: https://www.canva.com/design/DAF1T1bQpCY/fTDA7QpZbiFs7DWqxAQdVw/view?utm_content=DAF1T1bQpCY&utm_campaign=designshare&utm_medium=link&utm_source=editor

#  Situación Problemática:

En una plantación de aguacates, los agricultores están enfrentando pérdidas significativas debido a las variaciones climáticas extremas. Las fluctuaciones de temperatura han afectado el rendimiento de los aguacates, ya que ciertas variedades de aguacates son más sensibles a cambios específicos de temperatura durante su desarrollo.

En este escenario, el cultivo de aguacates requiere una gestión cuidadosa de las condiciones climáticas para maximizar el rendimiento y minimizar las pérdidas. Sin embargo, las predicciones meteorológicas actuales no son lo suficientemente específicas para las necesidades de este cultivo.
 
  
# PASOS:
BIBLIOTECAS:
- "pandas", Para trabajar con estructuras de datos tipo DataFrame.
- "train_test_split de sklearn.model_selection" Para dividir los datos en conjuntos de entrenamiento y prueba.
- "LinearRegression de sklearn.linear_model" Para crear y entrenar un modelo de regresión lineal.
- "matplotlib.pyplot" Para graficar los datos y el modelo.

- Se crea un DataFrame con dos columnas, 'Fecha' y 'Temperatura', que representan los datos de ejemplo.
Dividir los datos:

- Se dividen los datos en conjuntos de entrenamiento y prueba usando train_test_split.
Crear y entrenar el modelo:

- Se crea un objeto de modelo de regresión lineal (LinearRegression) y se entrena con los datos de entrenamiento.
Predecir temperaturas para nuevas fechas:

- Se utiliza el modelo entrenado para predecir las temperaturas para nuevas fechas.
Imprimir las predicciones:

- Se imprime en la consola las predicciones de temperaturas para las nuevas fechas.
Graficar el modelo:

- Se utiliza matplotlib para graficar los datos reales, el modelo de regresión lineal y las predicciones para nuevas fecha
  
# CODIGO 
# Código para predecir temperaturas basándose en fechas:
```
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


```
# Tabla Guia:
![image](https://github.com/LauraDa999/PROYECTO-FINAL/assets/141860731/0157d0b2-0902-47cc-bcd9-606fd72c413c)


# Temperaturaa ideales en el desaroolo de crecimiento de la planta
- Para la germinación de semillas de aguacate: rango de 25-30 
- Temperatura para el Crecimiento Vegetativo: entre 20-25 .
- Temperatura para la Floración: rango de 20-24 grados Celsius y temperaturas nocturnas que no desciendan significativamente por debajo de 10 grados Celsius.
- Temperatura para la Polinización y Desarrollo del Fruto: diurnas entre 20-25 grados Celsius suelen ser favorables.

# Herramientas utilizadas y vistas en el curso
Aquí hay algunos temas fundamentales que se pueden reconocer en el código:

#  Importación de Bibliotecas:
Se importan bibliotecas esenciales como pandas, sklearn, y matplotlib para manejar datos, realizar regresión lineal y crear visualizaciones.
```
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
```
# División de Datos:
Se dividen los datos en conjuntos de entrenamiento y prueba utilizando train_test_split de sklearn.
```
X_train, X_test, y_train, y_test = train_test_split(df[['Fecha']], df['Temperatura'], test_size=0.2, random_state=42)
```
# Interacción con el Usuario:
Se utiliza la función input para permitir que el usuario ingrese datos desde la consola.
```
fecha_7 = float(input("Ingrese la fecha para la predicción (por ejemplo, 7): "))
fecha_8 = float(input("Ingrese otra fecha para la predicción (por ejemplo, 8): "))
```
# Manejo de Errores:
Se implementa una estructura try...except para manejar errores en la entrada del usuario.
```

except ValueError:
    print("Error: Ingrese valores numéricos para las fechas.")
    exit()
```
# Predicciones y Visualizaciones:
Se realizan predicciones utilizando el modelo entrenado y se visualizan los resultados.
```
nuevas_fechas = pd.DataFrame({'Fecha': [fecha_7, fecha_8]})
predicciones = modelo.predict(nuevas_fechas)

plt.show()
```

# Uso del Modelo de Regresión Lineal:

Se decide utilizar un modelo de regresión lineal para predecir las temperaturas futuras con mayor precisión. El modelo utilizará datos históricos de temperaturas y fechas para prever los cambios climáticos esperados en el corto plazo.

Pasos:

- Recolección de Datos: Se recopilan datos históricos de temperaturas y fechas en la plantación de aguacates.
- Desarrollo del Modelo: Utilizando el código de regresión lineal, se desarrolla un modelo que relaciona las fechas con las temperaturas.
- Entrenamiento del Modelo: El modelo se entrena con datos históricos para aprender los patrones climáticos específicos de la plantación.
- Predicciones Futuras: El modelo se utiliza para prever las temperaturas futuras, especialmente durante períodos críticos de crecimiento del aguacate.
- Implementación de Estrategias: Con las predicciones en mano, los agricultores pueden implementar estrategias específicas, como ajustar el riego, aplicar protección contra heladas, o programar la - cosecha, para mitigar los efectos adversos de las condiciones climáticas.

#  Beneficios Esperados:
la plantación de aguacates, salvaria las pérdidas debidas a las variaciones climáticas extremas, se podrían esperar varios beneficios y mejoras en la gestión del cultivo.
| Beneficios | Descripcion|
| --- | --- |
| Reducción de Pérdidas por Condiciones Climáticas Desfavorables: | La capacidad de prever y anticipar las variaciones climáticas extremas permitirá a los agricultores tomar medidas preventivas para proteger los cultivos, reduciendo así las pérdidas asociadas a condiciones climáticas desfavorables. |
| Optimización de las Prácticas Agrícolas: | Con predicciones más precisas, los agricultores podrán ajustar sus prácticas agrícolas, como el riego y la fertilización, para adaptarse a las condiciones climáticas previstas, maximizando así el rendimiento y la salud de los aguacates. |
| Mejora en la Calidad de los Cultivos:  | Al gestionar de manera más eficiente las condiciones climáticas, se puede esperar una mejora en la calidad de los aguacates cosechados, lo que podría tener un impacto positivo en los precios de mercado.  |
| Planificación Estratégica de Cosechas: | La capacidad de prever las condiciones climáticas permitirá a los agricultores planificar de manera más estratégica la cosecha, eligiendo momentos óptimos para maximizar la calidad y cantidad de la producción. |
| Aumento de la Rentabilidad: | La reducción de pérdidas y la mejora en la calidad de los cultivos pueden contribuir directamente a un aumento en la rentabilidad de la plantación de aguacates. |
| Uso Eficiente de Recursos: | Al adaptar las prácticas agrícolas según las predicciones climáticas, se puede lograr un uso más eficiente de recursos como el agua y los fertilizantes, contribuyendo a la sostenibilidad del cultivo. |
| Generación de Conocimiento: | La implementación del proyecto no solo resolverá el problema inmediato, sino que también generará conocimiento valioso sobre la relación entre las condiciones climáticas y el rendimiento de los aguacates, lo cual puede ser útil para futuras investigaciones y mejoras. |
| Resiliencia ante Cambios Climáticos: | Al contar con un sistema de predicción y adaptación, la plantación de aguacates estará mejor preparada para enfrentar los desafíos planteados por los cambios climáticos, brindando mayor resiliencia a la operación agrícola. |


# GRACIAS





