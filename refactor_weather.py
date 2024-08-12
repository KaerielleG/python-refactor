# weather_data_fetcher.py

class WeatherDataFetcher:
    def fetch_weather_data(self, city):
        """Simulated method to fetch weather data for a given city"""
        print(f"Fetching weather data for {city}...")
        weather_data = {
            "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
            "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
            "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}
        }
        return weather_data.get(city, {})


class WeatherDataParser:
    def parse_weather_data(self, data):
        """Method to parse weather data"""
        if not data:
            return "Weather data not available"
        city = data["city"]
        temperature = data["temperature"]
        condition = data["condition"]
        humidity = data["humidity"]
        return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"

    def get_detailed_forecast(self, data):
        """Method to provide a detailed weather forecast"""
        return self.parse_weather_data(data)


class WeatherApp:
    def __init__(self):
        self.fetcher = WeatherDataFetcher()
        self.parser = WeatherDataParser()

    def display_weather(self, city):
        """Method to display the basic weather forecast for a city"""
        data = self.fetcher.fetch_weather_data(city)
        if not data:
            print(f"Weather data not available for {city}")
        else:
            weather_report = self.parser.parse_weather_data(data)
            print(weather_report)

    def run(self):
        """Main loop to run the weather application"""
        while True:
            city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
            if city.lower() == 'exit':
                break
            detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
            data = self.fetcher.fetch_weather_data(city)
            if detailed == 'yes':
                forecast = self.parser.get_detailed_forecast(data)
            else:
                forecast = self.parser.parse_weather_data(data)
            print(forecast)


if __name__ == "__main__":
    app = WeatherApp()
    app.run()
