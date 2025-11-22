import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

# relationship_app/query_samples.py

from relationship_app.models import Author, Book, Library, Librarian


# 1. Query all books by a specific author
def books_by_author(author_name):
    # First get the author object
    author = Author.objects.get(name=author_name)

    # Then query books using the author object
    books = Book.objects.filter(author=author)

    return books


# 2. List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()


# 3. Retrieve the librarian for a library
def librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian  # because OneToOneField gives direct access


# Run sample queries
if __name__ == "__main__":
    # Example: Query all books by an author
    author_name = "J.K. Rowling"
    books = books_by_author(author_name)
    print(f"Books by {author_name}:")
    for book in books:
        print(book.title)

    # Example: List all books in a library
    library_name = "Central Library"
    books = books_in_library(library_name)
    print(f"\nBooks in {library_name}:")
    for book in books:
        print(book.title)

    # Example: Retrieve librarian for a library
    librarian = librarian_for_library(library_name)
    print(f"\nLibrarian for {library_name}: {librarian.name}")
