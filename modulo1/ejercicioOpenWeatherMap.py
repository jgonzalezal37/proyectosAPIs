import requests

api_key = ""
ciudad = input("Introduce una ciudad: ")
url_peticion = f'https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}'

def getCiudad():
    response = requests.get(url_peticion).json()
    temperature_weather = [response['main']['temp'], response['weather'][0]['main']]
   
    return f'En {ciudad} la temperatura actual es de: {temperature_weather[0]} con un clima: {temperature_weather[1]}'

print(getCiudad())
