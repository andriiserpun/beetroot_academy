from django.db import models

class Author(models.Model):
    country_code = [
        ('UA', 'Ukraine'),
        ('US', 'USA'),
        ('PL', 'Poland'),
        ('FR', 'France'),
        ('DE', 'Germany'),
        ('ES', 'Spain')
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country = models.CharField(max_length=2, choices=country_code)

class Book(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    authors = models.ManyToManyField(Author, related_name="books", blank=True)
