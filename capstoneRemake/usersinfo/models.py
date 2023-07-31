import django
from django.db import models
from django.contrib.auth.models import User
from datetime import date
from teams.models import Team
from django.db.models.signals import post_save

roleChoices = (
    ("member", "member"),
    ("team lead", "team lead"),
    ("admin", "admin")
)


# Create your models here.
class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, default="member", choices=roleChoices)
    startDate = models.DateField(default = django.utils.timezone.now, verbose_name="Start date")
    team = models.ForeignKey(Team, on_delete=models.SET_DEFAULT, db_constraint=False, default=0)

def create_UserInfo(sender, instance, created, **kwargs):
    if created:
        userInfo = UserInfo(user=instance, id=instance.id)
        userInfo.save()

post_save.connect(create_UserInfo, sender=User)