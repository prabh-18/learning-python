import requests

def get_weather():
    # 1. Ask the user for the city name
    city = input("Enter the name of a city: ").strip()

    # Check if input is empty
    if not city:
        print("Error: City name cannot be empty.")
        return

    # 2. Define the URL (using format=j1 for a clean JSON response)
    url = f"http://wttr.in/{city}?format=j1"

    try:
        # 3. Make the HTTP GET request
        # Setting a timeout ensures the app doesn't hang if the site is down
        response = requests.get(url, timeout=10)

        # Raise an exception if the request returned an unsuccessful status code
        response.raise_for_status()

        # 4. Parse the JSON response
        data = response.json()

        # wttr.in returns data in specific nested lists. 
        # current_condition[0] contains the most recent weather data.
        current = data['current_condition'][0]
        
        # Extracting specific data points
        temp_c = current['temp_C']
        temp_f = current['temp_F']
        weather_desc = current['weatherDesc'][0]['value']
        humidity = current['humidity']
        wind_speed = current['windspeedKmph']
        feels_like = current['FeelsLikeC']

        # 5. Format the output nicely
        print("-" * 30)
        print(f"Weather Report for: {city.capitalize()}")
        print("-" * 30)
        print(f"Condition:    {weather_desc}")
        print(f"Temperature:  {temp_c}°C ({temp_f}°F)")
        print(f"Feels Like:   {feels_like}°C")
        print(f"Humidity:     {humidity}%")
        print(f"Wind Speed:   {wind_speed} km/h")
        print("-" * 30)

    # 6. Basic Error Handling
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the internet.")
    except requests.exceptions.HTTPError:
        print(f"Error: Could not find weather data for '{city}'. Please check the spelling.")
    except requests.exceptions.Timeout:
        print("Error: The server timed out. Please try again later.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    get_weather()