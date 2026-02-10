from django.urls import path
from .views import RoutePlannerAPIView
urlpatterns = [path('plan-route/', RoutePlannerAPIView.as_view())]
