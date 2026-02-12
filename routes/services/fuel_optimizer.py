# Fuel optimization logic
from .fuel_data import find_cheapest_station

MAX_RANGE_MILES = 500
MPG = 10


def calculate_fuel(total_distance_miles):
    AVERAGE_MPG = 30
    FUEL_PRICE_PER_LITER = 105  # INR, example

    gallons_used = total_distance_miles / AVERAGE_MPG
    liters_used = gallons_used * 3.785
    total_cost = liters_used * FUEL_PRICE_PER_LITER

    return {
        "liters": round(liters_used, 2),
        "cost": round(total_cost, 2)
    }

