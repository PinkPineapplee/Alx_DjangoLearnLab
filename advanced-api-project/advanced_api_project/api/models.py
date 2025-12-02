from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)


class Book(models.Model):
    name = models.CharField(max_length = 150)
    author = models.ForeignKey(Author) 
    release_date = models.DateField()
    borrowed_date = models.DateField()   