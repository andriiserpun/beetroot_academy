import requests

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather_info = f"Weather in {city_name}: {weather_description}\n"
        weather_info += f"Temperature: {temperature}°C\n"
        weather_info += f"Humidity: {humidity}%"
        return weather_info
    else:
        return "Error fetching weather data"

def main():
    api_key = "30341c06743084e601ef0a193c759155"
    city_name = input("Введите название города: ")

    weather_info = get_weather(city_name, api_key)
    print(weather_info)

if __name__ == "__main__":
    main()
