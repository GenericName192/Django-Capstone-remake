from django.urls import path
from locations.views import locations, locationCreate, locationDetail, locationUpdate, locationDelete

urlpatterns = [
    path("locations", locations, name="locations"),
    path("location-detail/<int:id>", locationDetail, name="locationDetail"),
    path("create-location", locationCreate, name="locationCreate"),
    path("location-update/<int:id>", locationUpdate, name="locationUpdate"),
    path("location-delete/<int:id>", locationDelete, name="locationDelete"),
]