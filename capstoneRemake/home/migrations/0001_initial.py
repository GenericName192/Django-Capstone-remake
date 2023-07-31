# Generated by Django 4.2.3 on 2023-07-27 16:26

from django.db import migrations


def generateUnassigned(apps, schema_editor):
    location = apps.get_model("locations", "Location")
    WYWMHQ = location(id = 0, name = "WYWM HQ", task = "training")
    WYWMHQ.save()
    team = apps.get_model("teams", "Team")
    UnassignedTeam = team(id = 0, name = "Unassigned", location_id = 0)
    UnassignedTeam.save()

class Migration(migrations.Migration):

    dependencies = [("locations", "0001_initial"), 
                    ("teams", "0001_initial")]

    operations = [migrations.RunPython(generateUnassigned),]
