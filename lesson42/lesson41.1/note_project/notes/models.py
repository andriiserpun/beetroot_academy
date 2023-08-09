from django.db import models

# Create your models here.
from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    reminder = models.CharField(max_length=100)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title
