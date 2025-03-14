import requests

API_KEY = '671e54de6524506060d19c12a5c071b7'
city =  'Tashkent'
URL = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

def get_weather():
    try:
        response = requests.get(URL)
        data = response.json()

        if response.status_code == 200:
            weather_info = {
                "City": data["name"],
                "Temperature": f"{data['main']['temp']}°C",
                "Humidity": f"{data['main']['humidity']}%",
                "Weather": data["weather"][0]["description"].title(),
                "Wind Speed": f"{data['wind']['speed']} m/s"
            }

            print("\nWeather in Tashkent:")
            for key, value in weather_info.items():
                print(f"{key}: {value}")

        else:
            print(f"Error: {data['message']}")

    except Exception as e:
        print("Failed to retrieve weather data:", str(e))

get_weather()