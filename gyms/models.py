from django.db import models


# Create your models here.
class Gym(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    Address = models.CharField(max_length=50)
    Contacts = models.TextField()

    def __str__(self):
        return self.name


class Trainer(models.Model):
    gym = models.ForeignKey(Gym, related_name='trainer', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField(default=0)
