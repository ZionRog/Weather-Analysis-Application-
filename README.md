Weather Analysis Application

Technologies Used

- Python
- SQLAlchemy
- SQLite
- Open-Meteo API
  
Description:
This application retrieves historical weather data using the Open-Meteo API for a selected U.S. location and date. It calculates five-year averages for temperature, wind speed, and precipitation, stores the data in a SQLite database using SQLAlchemy, and allows the user to query the stored weather record.

Requirements:
- Python 3.11 or newer
- requests
- sqlalchemy
- sqlite

Setup Instructions:
1. Clone the repository to your local machine.
2. Install the required packages:

   pip install -r requirements.txt

3. Run the main program:

   python main.py

Inputs:
The latitude, longitude, month, day, and year can be modified in main.py when creating the WeatherData object.

Example:
WeatherData(42.116964974527036, -80.052278, 10, 10, 2025)

Outputs:
- Prints the calculated five-year weather statistics to the console.
- To do something with this data, run weather_table and then run db_query_file.py 
