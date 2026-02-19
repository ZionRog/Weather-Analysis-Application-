import requests
class WeatherData:
    def __init__(self, latitude, longitude, month, dayOfMonth, year):
        self.latitude = latitude
        self.longitude = longitude
        self.month = month
        self.dayOfMonth = dayOfMonth
        self.year = year
        self.averageTemp5Year = None
        self.minTemp5Year = None
        self.maxTemp5Year = None
        self.averageWindSpeed5Year = None
        self.minWindSpeed5Year = None
        self.maxWindSpeed5Year = None
        self.sumPrecipitation5Year = None
        self.minPrecipitation5Year = None
        self.maxPrecipitation5Year = None

# Formats month/day as "MM-DD" so we can filter the returned dates easily.
    def _format_mm_dd(self):
        return f"{int(self.month):02d}-{int(self.dayOfMonth):02d}"

# Calls the Open-Meteo API and returns only the rows matching the chosen month/day

    def _fetch_last_five_years_daily(self):
        url = "https://archive-api.open-meteo.com/v1/archive"
        end_year = int(self.year)
        start_year = end_year - 4

        # Build the 5-year date range for the selected month/day

        mm_dd = self._format_mm_dd()
        start_date = f"{start_year}-{mm_dd}"
        end_date = f"{end_year}-{mm_dd}"

        params = {
            "latitude": self.latitude,
            "longitude": self.longitude,
            "start_date": start_date,
            "end_date": end_date,
            "daily": [
                "temperature_2m_max",
                "temperature_2m_min",
                "wind_speed_10m_max",
                "wind_speed_10m_min",
                "precipitation_sum"
            ],
            "timezone": "auto",
            "temperature_unit": "fahrenheit",
            "wind_speed_unit": "mph",
            "precipitation_unit": "inch",
        }

        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        daily = data.get("daily", {})
        dates = daily.get("time", [])
        temps_max = daily.get("temperature_2m_max", [])
        temps_min = daily.get("temperature_2m_min", [])
        winds_max = daily.get("wind_speed_10m_max", [])
        winds_min = daily.get("wind_speed_10m_min", [])
        precip = daily.get("precipitation_sum", [])

        target_mm_dd = mm_dd
        rows = []

        for i in range(len(dates)):
            d = dates[i]
            if d[5:] == target_mm_dd:
                rows.append({
                    "date": d,
                    "tempMax": temps_max[i],
                    "tempMin": temps_min[i],
                    "windMax": winds_max[i],
                    "windMin": winds_min[i],
                    "precip": precip[i]
                })

        self._oct_rows = rows
        return rows

    def calculate_mean_temperature_f(self):
        rows = self._fetch_last_five_years_daily()
        temp_max_values = []
        temp_min_values = []

        for row in rows:
            temp_max_values.append(row["tempMax"])
            temp_min_values.append(row["tempMin"])

        daily_mean_values = []
        for i in range(len(temp_max_values)):
            daily_mean_values.append((temp_max_values[i] + temp_min_values[i]) / 2)

        self.averageTemp5Year = sum(daily_mean_values) / len(daily_mean_values)
        self.minTemp5Year = min(daily_mean_values)
        self.maxTemp5Year = max(daily_mean_values)

        return self.averageTemp5Year

    def calculate_maximum_wind_mph(self):
        rows = self._fetch_last_five_years_daily()
        temp_max_values = []

        for i in range(len(rows)):
            temp_max_values.append(rows[i]["windMax"])

        maximum = max(temp_max_values)
        self.maxWindSpeed5Year = maximum
        return self.maxWindSpeed5Year

    def precipitation_sum_inches(self):
        rows = self._fetch_last_five_years_daily()
        temp_max_values = []

        for i in range(len(rows)):
            temp_max_values.append(rows[i]["precip"])

        sum_of_values = sum(temp_max_values)
        self.sumPrecipitation5Year = sum_of_values

        return self.sumPrecipitation5Year



