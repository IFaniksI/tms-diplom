from django.db import models


# Create your models here.
class Article(models.Model):
    image = models.ImageField(upload_to='images/', null=True)
    title = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.title