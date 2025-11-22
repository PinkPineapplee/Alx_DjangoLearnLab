from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library


# Function-based view: list all books
def list_books(request):
    """
    Reach into the DB and pull every Book record, then render a simple list.
    """
    books = Book.objects.select_related('author').all()  # efficient FK fetch
    return render(request, 'relationship_app/list_books.html', {'books': books})


# Class-based view — display details for a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
