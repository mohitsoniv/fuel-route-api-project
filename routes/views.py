from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .services.routing import get_route


class RoutePlannerAPIView(APIView):
    def post(self, request):
        start = request.data.get("start")
        end = request.data.get("end")

        if not start or not end:
            return Response(
                {"error": "start or end missing"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if "lat" not in start or "lng" not in start:
            return Response(
                {"error": "start must contain lat and lng"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if "lat" not in end or "lng" not in end:
            return Response(
                {"error": "end must contain lat and lng"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # 🔹 CALL ROUTING SERVICE
        route = get_route(start, end)

        return Response(
            {
                "route": route
            },
            status=status.HTTP_200_OK
        )

