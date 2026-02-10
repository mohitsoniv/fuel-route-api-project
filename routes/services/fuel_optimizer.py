# Fuel optimization logic
from .fuel_data import find_cheapest_station

MAX_RANGE_MILES = 500
MPG = 10


def calculate_fuel(route_coords, total_distance_miles):
    """
    Calculate optimal fuel stops and total fuel cost
    """

    stops = []
    total_cost = 0.0
    distance_since_last_fill = 0.0

    # rough approximation: each coordinate step ~10 miles
    STEP_MILES = 10

    for lng, lat in route_coords:
        distance_since_last_fill += STEP_MILES

        if distance_since_last_fill >= MAX_RANGE_MILES:
            station = find_cheapest_station(lat, lng)

            if station:
                gallons = MAX_RANGE_MILES / MPG
                cost = gallons * station["price"]

                stops.append({
                    "station": station,
                    "gallons": round(gallons, 2),
                    "cost": round(cost, 2),
                })

                total_cost += cost

            distance_since_last_fill = 0.0

    return stops, round(total_cost, 2)
