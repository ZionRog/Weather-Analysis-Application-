from sqlalchemy import create_engine, Column, Integer, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# SQLAlchemy ORM model for storing the summarized 5-year weather values in SQLite

class WeatherRecords(Base):
    __tablename__ = "weather_records"

    id = Column(Integer, primary_key=True, autoincrement=True)

    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

    month = Column(Integer, nullable=False)
    day_of_month = Column(Integer, nullable=False)
    year = Column(Integer, nullable=False)

    avg_temp_5yr = Column(Float)
    min_temp_5yr = Column(Float)
    max_temp_5yr = Column(Float)

    avg_wind_5yr = Column(Float)
    min_wind_5yr = Column(Float)
    max_wind_5yr = Column(Float)

    sum_precip_5yr = Column(Float)
    min_precip_5yr = Column(Float)
    max_precip_5yr = Column(Float)

def get_engine(db_path: str = "sqlite:///weather.db"):
    return create_engine(db_path, echo=False, future=True)

print("Connecting to database...")
print("Connected to database, engine also created for database.")
