from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length = 100)



class Book(models.Model):
    title = models.CharField(max_length = 150)
    author = models.ForeignKey(Author) 
    publication_year = models.DateField()
    borrowed_date = models.DateField()   