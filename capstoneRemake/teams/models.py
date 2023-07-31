from django.db import models
from locations.models import Location

class Team(models.Model):
    name = models.CharField(max_length=30)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name