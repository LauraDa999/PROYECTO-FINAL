# PROYECTO-FINAL
#  "Análisis de Datos Climáticos EN CULTIVOS AGRICOLAS" - Alternativa#3
#  Equipo Code-farmers
PRESENTADO POR:
LAURA DANIELA GARCIA CHAVES Y MARIA JOSE VALLEJO RODRIGUEZ

#  Situación Problemática:

En una plantación de aguacates, los agricultores están enfrentando pérdidas significativas debido a las variaciones climáticas extremas. Las fluctuaciones de temperatura han afectado el rendimiento de los aguacates, ya que ciertas variedades de aguacates son más sensibles a cambios específicos de temperatura durante su desarrollo.

En este escenario, el cultivo de aguacates requiere una gestión cuidadosa de las condiciones climáticas para maximizar el rendimiento y minimizar las pérdidas. Sin embargo, las predicciones meteorológicas actuales no son lo suficientemente específicas para las necesidades de este cultivo.

# CODIGO ORIGINAL
# Código específicamente para crear un modelo para predecir temperaturas basándose en fechas:
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
# Manipulación de Datos con Pandas:
Se utiliza la biblioteca pandas para crear un DataFrame a partir de datos ficticios.
```
data = {'Fecha': [1, 2, 3, 4, 5, 6],
        'Temperatura': [25, 28, 24, 30, 32, 29]}
df = pd.DataFrame(data)
```
# División de Datos:
Se dividen los datos en conjuntos de entrenamiento y prueba utilizando train_test_split de sklearn.
```
X_train, X_test, y_train, y_test = train_test_split(df[['Fecha']], df['Temperatura'], test_size=0.2, random_state=42)
```
# Creación y Entrenamiento de un Modelo de Regresión Lineal:
Se crea un modelo de regresión lineal y se entrena con datos de entrenamiento.

```
modelo = LinearRegression()
modelo.fit(X_train, y_train)
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

- Optimización del Riego: Mejor gestión del riego basada en las predicciones de temperaturas, evitando el estrés hídrico o el exceso de agua.
- Planificación de Cosecha: Programación de la cosecha en momentos óptimos, considerando las condiciones climáticas favorables para la calidad del aguacate.
- Reducción de Pérdidas: Minimización de pérdidas debidas a eventos climáticos extremos mediante acciones preventivas informadas por el modelo.






