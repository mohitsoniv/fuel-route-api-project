def calculate_fuel(distance_km, mileage_kmpl=12, price_per_liter=105):
    fuel_liters = distance_km / mileage_kmpl
    fuel_cost = fuel_liters * price_per_liter

    return {
        "liters": round(fuel_liters, 2),
        "cost": round(fuel_cost, 2)
    }
