In [4]: book = Book.objects.get(title="1984")

In [5]: book.title = "Nineteen Eighty-Four"

In [6]: book.save()

In [7]: book.title
Out[7]: 'Nineteen Eighty-Four'