from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .services.routing import get_route
from .services.fuel_optimizer import calculate_fuel


class RoutePlannerAPIView(APIView):
    def post(self, request):
        start = request.data.get("start")
        end = request.data.get("end")

        if not start or not end:
            return Response(
                {"error": "start and end are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Get route info
        route = get_route(start, end)

        # Calculate fuel (distance in miles)
        fuel = calculate_fuel(
            total_distance_miles=route["distance_km"] * 0.621371
        )

        return Response(
            {
                "status": "success",
                "data": {
                    "route": route,
                    "fuel": fuel,
                },
            },
            status=status.HTTP_200_OK,
        )

