from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
       return self.name
class Book(models.Model):
    title = models.CharField(max_length = 250)
    author = models.ForeignKey(Author, on_delete =models.CASCADE, related_name = 'books') 
    publication_year = models.DateField()
    borrowed_date = models.DateField()   

    def __str__(self):
        return self.title