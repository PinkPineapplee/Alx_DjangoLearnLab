In [1]: from bookshelf.models import Book
   ...: 
   ...: book = Book.objects.create(
   ...:     title="1984",
   ...:     author="George Orwell",
   ...:     publication_year=1949
   ...: )
   ...: book
   ...: 
Out[1]: <Book: 1984>

In [2]: book = Book.objects.get(title="1984")

In [3]: book.title, book.author, book.publication_year
Out[3]: ('1984', 'George Orwell', 1949)

In [4]: book = Book.objects.get(title="1984")

In [5]: book.title = "Nineteen Eighty-Four"

In [6]: book.save()

In [7]: book.title
Out[7]: 'Nineteen Eighty-Four'

In [8]: book = Book.objects.get(title="Nineteen Eighty-Four")
   ...: book.delete()
   ...: 
   ...: Book.objects.all()
Out[8]: <QuerySet []>

In [9]: 