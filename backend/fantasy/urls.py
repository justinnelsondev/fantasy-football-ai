from django.urls import path
from .views import health, league

urlpatterns = [
    path("health/", health),
    path("league/", league),
]