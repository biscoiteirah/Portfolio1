import requests
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
API_KEY = os.getenv('OPENWEATHER_API_KEY')

# Debugging: Print the API Key to verify it's loaded
print(f"API Key: {API_KEY}")

def get_weather_forecast(city):
    if not API_KEY:
        return "Erro: A chave da API não foi encontrada. Verifique o arquivo .env."

    # Get latitude and longitude for the city
    geocode_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}"
    geocode_response = requests.get(geocode_url)
    
    if geocode_response.status_code != 200 or not geocode_response.json():
        return "Erro: Cidade não encontrada ou problema na API de geocodificação."
    
    geocode_data = geocode_response.json()
    if len(geocode_data) == 0:
        return "Erro: Cidade não encontrada."
    
    lat = geocode_data[0]['lat']
    lon = geocode_data[0]['lon']

    # Get the weather forecast for the city
    forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units=metric&appid={API_KEY}"
    forecast_response = requests.get(forecast_url)
    
    if forecast_response.status_code != 200:
        return "Erro: Não foi possível obter a previsão do tempo."
    
    forecast_data = forecast_response.json()
    daily_forecast = forecast_data.get('list', [])
    
    if not daily_forecast:
        return "Erro: Dados de previsão não disponíveis."
    
    # Process the forecast data to get one entry per day
    results = []
    seen_dates = set()  # To track processed dates
    for day in daily_forecast:
        date = datetime.fromtimestamp(day['dt']).strftime('%d-%m-%Y')
        if date not in seen_dates:  # Only process the first entry for each day
            seen_dates.add(date)
            temp = day['main']['temp']
            description = day['weather'][0]['description'].capitalize()
            humidity = day['main']['humidity']
            wind = day['wind']['speed']
            
            results.append(
                f"{date}: {description}\n"
                f"Temperatura: {temp}°C | Umidade: {humidity}% | Vento: {wind} m/s\n"
            )
    
    return results

# Main program
if __name__ == "__main__":
    city = input("Digite o nome da cidade: ")
    forecast = get_weather_forecast(city)
    
    if isinstance(forecast, list):
        print(f"\nPrevisão para {city}:\n")
        for day in forecast:
            print(day)
    else:
        print(forecast)