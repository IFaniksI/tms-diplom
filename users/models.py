from time import timezone

from django.db import models

from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Permission(models.Model):
    profile = models.ForeignKey(Profile, related_name='profile', on_delete=models.CASCADE)
    gym_name = models.CharField(max_length=50, null=True)
    service_name = models.CharField(max_length=50)
    subscription_name = models.CharField(max_length=50, null=True)
    start_date = models.DateField()
    end_date = models.DateField()

