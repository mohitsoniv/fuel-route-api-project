import os
import requests
from requests.exceptions import ReadTimeout, RequestException

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

    try:
        r = requests.post(
            url,
            json=body,
            headers=headers,
            timeout=30   # ⬅ increased timeout
        )
        r.raise_for_status()
        data = r.json()

        if "routes" not in data:
            return {"error": "ORS returned no route"}

        summary = data["routes"][0]["summary"]

        return {
            "distance_km": round(summary["distance"] / 1000, 2),
            "duration_hours": round(summary["duration"] / 3600, 2),
        }

    except ReadTimeout:
        return {"error": "Route service timeout. Try again."}

    except RequestException as e:
        return {"error": "Route service error", "details": str(e)}

