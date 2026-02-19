from weather_data import WeatherData

# Creates a WeatherData instance for the selected location/date and prints the 5-year summaries.

oct10 = WeatherData(42.116964974527036, -80.052278, 10, 10,2025)

print(oct10.calculate_mean_temperature_f())
print(oct10.calculate_maximum_wind_mph())
print(oct10.precipitation_sum_inches())
