from django.contrib.auth.models import User

# Create your models here.
from django.db import models

class Movie(models.Model):
    user_first_name = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    country = models.CharField(max_length=50)
    comment = models.TextField()
    viewed = models.BooleanField(default=False)


    def __str__(self):
        return self.title

