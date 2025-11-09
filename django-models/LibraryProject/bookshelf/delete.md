In [1]: from bookshelf.models import Book
In [8]: book = Book.objects.get(title="Nineteen Eighty-Four")
   ...: book.delete()
   ...: 
   ...: Book.objects.all()
Out[8]: <QuerySet []>
