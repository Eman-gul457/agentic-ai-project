import requests

def get_weather(city):
    try:
        url = f"https://wttr.in/{city}?format=j1"
        data = requests.get(url).json()

        current = data["current_condition"][0]
        temp = current["temp_C"]
        desc = current["weatherDesc"][0]["value"]

        return f"The weather in {city.title()} is {temp}°C with {desc}."
    except:
        return "Sorry, I could not fetch the weather data."
