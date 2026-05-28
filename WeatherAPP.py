
import requests
import matplotlib.pyplot as plt

API_KEY ="1ccb098c6c0fe1fccf9f6a95736daccf"

while True:

    city = input("\nEnter city name (or type 'exit' to quit): ")

    # Exit condition
    if city.lower() == "exit":
        print("Program ended.")
        break

    # API URL
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    # Send request
    response = requests.get(url)

    # Convert to dictionary
    data = response.json()

    # Check success
    if response.status_code == 200:

        main = data["main"]
        weather = data["weather"][0]

        temperature = main["temp"]
        humidity = main["humidity"]
        description = weather["description"]

        print("\n------ Weather Report ------")
        print(f"City: {city.upper()}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {description}")

        labels = ["Temperature (°C)", "Humidity (%)"]
        values = [temperature, humidity]

        plt.bar(labels, values)

        plt.title(f"Weather Report of {city.upper()}")

        plt.ylabel("Values")

        plt.show()

    else:
        print("\nError:", data["message"])


