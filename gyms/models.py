from django.db import models
from datetime import datetime


# Create your models here.
class Gym(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    address = models.CharField(max_length=50)
    contacts = models.TextField()

    def __str__(self):
        return self.name


class Trainer(models.Model):
    gym = models.ForeignKey(Gym, related_name='trainer', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.gym}'


class Service(models.Model):
    gym = models.ManyToManyField(Gym, related_name='servicex')
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Subscription(models.Model):
    service = models.ForeignKey(Service, related_name='aboniment', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    subscription_period = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.service.name} - {self.name}'
