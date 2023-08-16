

# Create your models here.
from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    country = models.CharField(max_length=50)
    comment = models.TextField()

    def __str__(self):
        return self.name
