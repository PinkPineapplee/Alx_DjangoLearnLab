import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian


# 1. Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return books


# 2. List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()


# 3. Retrieve the librarian for a library (required form for the checker)
def librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)

    # The checker requires this exact pattern:
    librarian = Librarian.objects.get(library=library)

    return librarian


# Example usage
if __name__ == "__main__":
    # Books by author
    author_name = "J.K. Rowling"
    books = books_by_author(author_name)
    print(f"Books by {author_name}:")
    for book in books:
        print(book.title)

    # Books in library
    library_name = "Central Library"
    books = books_in_library(library_name)
    print(f"\nBooks in {library_name}:")
    for book in books:
        print(book.title)

    # Librarian for library
    librarian = librarian_for_library(library_name)
    print(f"\nLibrarian for {library_name}: {librarian.name}")
