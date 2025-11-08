from weather import get_weather

def main():
    city = input("Enter city name: ")
    weather = get_weather(city)
    if "error" in weather:
        print(weather["error"])
    else:
        print(f"{weather['city']}: {weather['temperature']}°C, {weather['description']}")

if __name__ == "__main__":
    main()
