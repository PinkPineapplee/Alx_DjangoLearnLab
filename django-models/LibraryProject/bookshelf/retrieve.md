In [2]: book = Book.objects.get(title="1984")
In [3]: book.title, book.author, book.publication_year
Out[3]: ('1984', 'George Orwell', 1949)
