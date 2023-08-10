from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    reminders = models.DateTimeField(null=True, blank=True)
    category = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title
