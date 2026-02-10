import os
import requests

ORS_API_KEY = os.getenv("ORS_API_KEY")

def get_route(start, end):
    if not ORS_API_KEY:
        raise RuntimeError("ORS_API_KEY not set")

    url = "https://api.openrouteservice.org/v2/directions/driving-car"

    headers = {
        "Authorization": ORS_API_KEY,
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    body = {
        "coordinates": [
            [start["lng"], start["lat"]],
            [end["lng"], end["lat"]],
        ]
    }

    r = requests.post(url, json=body, headers=headers, timeout=15)
    r.raise_for_status()
    data = r.json()

    # ✅ HANDLE NON-GEOJSON RESPONSE
    if "routes" in data:
        summary = data["routes"][0]["summary"]
        return {
            "distance_km": round(summary["distance"] / 1000, 2),
            "duration_hours": round(summary["duration"] / 3600, 2),
        }

    # ❌ fallback (defensive)
    raise RuntimeError("ORS did not return route")

