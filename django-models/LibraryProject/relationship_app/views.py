from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library


# 1️⃣ Function-based view — list all books
def list_books(request):
    books = Book.objects.select_related('author').all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


# 2️⃣ Class-based view — display details for a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
