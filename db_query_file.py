from weather_table import Base, get_engine, WeatherRecords
from main import oct10
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select

engine = get_engine()
Base.metadata.create_all(engine)

print("Database and tables created.")

#Creating a record to insert into the database

record = WeatherRecords(
    latitude=oct10.latitude,
    longitude=oct10.longitude,
    month=oct10.month,
    day_of_month=oct10.dayOfMonth,
    year = oct10.year,
    avg_temp_5yr=oct10.averageTemp5Year,
    min_temp_5yr=oct10.minTemp5Year,
    max_temp_5yr=oct10.maxTemp5Year,
    avg_wind_5yr=oct10.averageWindSpeed5Year,
    min_wind_5yr=oct10.minWindSpeed5Year,
    max_wind_5yr=oct10.maxWindSpeed5Year,
    sum_precip_5yr=oct10.sumPrecipitation5Year,
    min_precip_5yr=oct10.minPrecipitation5Year,
    max_precip_5yr=oct10.maxPrecipitation5Year,
)

Session = sessionmaker(bind=engine)
session = Session()

# Inserting a record into SQLite database

try:
    session.add(record)
    session.commit()
    session.refresh(record)
    print(f"Inserted record {record.id} into database.")

    stmt = select(WeatherRecords).where(WeatherRecords.id == record.id)
    result = session.execute(stmt).scalar_one_or_none()

    if result is None:
        print("No record found.")
    else:
        print("Record selected successfully.")
        print(f"ID: {result.id}")
        print(f"Location: ({result.latitude}, {result.longitude})")
        print(f"Date: {result.year}-{result.month:02d}-{result.day_of_month:02d}")
        print(f"Avg Temp (5yr): {result.avg_temp_5yr:.2f} F")
        print(f"Min Temp (5yr): {result.min_temp_5yr:.2f} F")
        print(f"Max Temp (5yr): {result.max_temp_5yr:.2f} F")
        print(f"Avg Wind (5yr): {result.avg_wind_5yr}")
        print(f"Min Wind (5yr): {result.min_wind_5yr}")
        print(f"Max Wind (5yr): {result.max_wind_5yr:.2f} mph")
        print(f"Sum Precip (5yr): {result.sum_precip_5yr:.2f} inches")
        print(f"Min Precip (5yr): {result.min_precip_5yr}")
        print(f"Max Precip (5yr): {result.max_precip_5yr}")

except Exception as e:
    session.rollback()
    print(e)
finally:
    session.close()