from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import UserInfo
from teams.models import Team
from locations.models import Location

# Register your models here.
admin.site.unregister(Group)
admin.site.register(UserInfo)
admin.site.register(Team)
admin.site.register(Location)