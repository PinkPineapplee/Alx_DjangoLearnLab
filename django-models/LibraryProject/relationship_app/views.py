from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library


# Function-based view — list all books
def book_list(request):
      """Retrieves all books and renders a template displaying the list."""
      books = Book.objects.all()  # Fetch all book instances from the database
      context = {'book_list': books}  # Create a context dictionary with book list
      return render(request, 'books/list_book.html', context)


#Class-based view — display details for a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
