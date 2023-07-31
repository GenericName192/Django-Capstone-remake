from django.urls import path
from teams.views import teamCreate, teamDelete, teamDetail, teamUpdate

urlpatterns = [
    path("create", teamCreate, name="teamCreate"),
    path("detail/<int:id>", teamDetail, name="teamDetail"),
    path("update/<int:id>", teamUpdate, name="teamUpdate"),
    path("delete/<int:id>", teamDelete, name="teamDelete"),
    
]