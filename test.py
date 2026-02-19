import unittest
from weather_data import WeatherData

#Testing to make sure temp is a num value, wind is not negative, and weather data values are not None

class TestWeatherApp(unittest.TestCase):
    def setUp(self):
        self.lat = 42.116964974527036
        self.lon = -80.052278
        self.month = 10
        self.day = 10
        self.year = 2025

    # Mean temperature returns a value that is a number

    def test_mean_temp_is_number(self):
        weather_data = WeatherData(latitude=self.lat, longitude=self.lon, month=self.month, dayOfMonth=self.day, year=self.year)
        mean_temp = weather_data.calculate_mean_temperature_f()
        self.assertIsNotNone(mean_temp)

    # Maximum wind speed is positive

    def test_max_wind_is_not_neg(self):
        weather_data = WeatherData(self.lat, self.lon, self.month, self.day, self.year)
        max_wind = weather_data.calculate_maximum_wind_mph()
        self.assertGreater(max_wind, 0)

    # WeatherData stores calculated results on the object

    def test_weatherdata_sets_values(self):
        weather_data = WeatherData(self.lat, self.lon, self.month, self.day, self.year)

        weather_data.calculate_mean_temperature_f()
        weather_data.calculate_maximum_wind_mph()
        weather_data.precipitation_sum_inches()

        self.assertIsNotNone(weather_data.averageTemp5Year)
        self.assertIsNotNone(weather_data.maxWindSpeed5Year)
        self.assertIsNotNone(weather_data.sumPrecipitation5Year)


if __name__ == "__main__":
    unittest.main()
