import requests

def obtener_clima(api_key, latitud, longitud, año, mes, dia):
    # Configura la URL de la API de OpenWeatherMap
    url = "http://api.openweathermap.org/data/2.5/weather"
    
    # Parámetros de la solicitud
    parametros = {
        'lat': latitud,
        'lon': longitud,
        'appid': api_key,
        'units': 'metric',  # Puedes cambiar a 'imperial' para unidades Fahrenheit
    }

    # Realizar la solicitud a la API de OpenWeatherMap
    respuesta = requests.get(url, params=parametros)
    datos_clima = respuesta.json()

    # Verificar si la solicitud fue exitosa (código de estado 200)
    if respuesta.status_code == 200:
        # Imprimir información relevante (puedes personalizar esto según tus necesidades)
        print(f"\nClima en ({latitud}, {longitud}) para la fecha {año}-{mes}-{dia}:")
        print(f"Descripción: {datos_clima['weather'][0]['description']}")
        print(f"Temperatura: {datos_clima['main']['temp']}°C")
        print(f"Humedad: {datos_clima['main']['humidity']}%")
        print(f"Velocidad del viento: {datos_clima['wind']['speed']} m/s")
    else:
        print(f"\nNo se pudo obtener datos para la fecha {año}-{mes}-{dia}. Código de estado: {respuesta.status_code}")

# Configurar tu clave de API de OpenWeatherMap
api_key = '8111cbcf2acc2df1f441918b49af8429'

# Configurar las coordenadas (por ejemplo, Ciudad de México)
latitud = 4.924203
longitud = -75.055239

# Solicitar al usuario ingresar día, mes y año
dia = input("Ingresa el día: ")
mes = input("Ingresa el mes: ")
año = input("Ingresa el año: ")

# Obtener y mostrar el clima para la fecha ingresada
obtener_clima(api_key, latitud, longitud, año, mes, dia)
