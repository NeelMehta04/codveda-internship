import requests

city = "Mumbai"
url = f"https://wttr.in/{city}?format=j1"

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    current_condition = data['current_condition'][0]
    temperature = current_condition['temp_C']
    weather_desc = current_condition['weatherDesc'][0]['value']
    humidity = current_condition['humidity']

    print(f"Weather in {city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Condition: {weather_desc}")
    print(f"Humidity: {humidity}%")

except requests.exceptions.RequestException as e:
    print("Error fetching weather data:", e)
except KeyError:
    print("Unexpected response format.")