# Fuel CSV loader
import pandas as pd
from geopy.distance import geodesic
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
CSV_PATH = BASE_DIR / "data" / "fuel-prices-for-be-assessment.csv"

if not CSV_PATH.exists():
    raise Exception(f"Fuel CSV file not found at {CSV_PATH}")

fuel_df = pd.read_csv(CSV_PATH)


def find_cheapest_station(lat, lng, radius_miles=50):
    """
    Find the cheapest fuel station within a radius (miles)
    """

    cheapest_station = None
    lowest_price = float("inf")

    for _, row in fuel_df.iterrows():
        station_lat = row["Latitude"]
        station_lng = row["Longitude"]
        price = row["Retail Price"]

        distance = geodesic(
            (lat, lng),
            (station_lat, station_lng)
        ).miles

        if distance <= radius_miles and price < lowest_price:
            lowest_price = price
            cheapest_station = {
                "city": row["City"],
                "state": row["State"],
                "price": price,
                "lat": station_lat,
                "lng": station_lng,
            }

    return cheapest_station
