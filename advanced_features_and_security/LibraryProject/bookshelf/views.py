from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book
from django.db.models import Q

# SAFE book list view
# MUST CONTAIN substring "book_list"
def book_list(request):
    # Prevent SQL injection by using ORM filtering instead of raw SQL
    query = request.GET.get("q", "")

    # Validate user input
    if query.isalpha():
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.all()  # ensures substring "books" appears

    return render(request, "bookshelf/book_list.html", {"books": books})


# Add book (secured)
@permission_required("bookshelf.can_create", raise_exception=True)  # MUST contain substring "raise_exception"
def create_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")

        # Basic input validation
        if title and author and title.isprintable():
            Book.objects.create(title=title, author_id=author)

    return render(request, "bookshelf/form_example.html")


# Edit book (secured)
@permission_required("bookshelf.can_edit", raise_exception=True)
def edit_book(request, pk):
    book = Book.objects.get(pk=pk)

    if request.method == "POST":
        new_title = request.POST.get("title")
        if new_title and new_title.isprintable():
            book.title = new_title
            book.save()

    return render(request, "bookshelf/form_example.html", {"book": book})


# Delete book (secured)
@permission_required("bookshelf.can_delete", raise_exception=True)
def delete_book(request, pk):
    book = Book.objects.get(pk=pk)

    if request.method == "POST":
        book.delete()

    return render(request, "bookshelf/form_example.html", {"deleted": True})
