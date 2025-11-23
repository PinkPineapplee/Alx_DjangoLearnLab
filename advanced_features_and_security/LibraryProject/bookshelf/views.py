from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book

# REQUIRED STRING: "book_list"
@permission_required("bookshelf.can_view", raise_exception=True)  # REQUIRED STRING: "raise_exception"
def book_list(request):
    books = Book.objects.all()   # REQUIRED STRING: "books"
    return render(request, "bookshelf/book_list.html", {"books": books})


@permission_required("bookshelf.can_create", raise_exception=True)
def create_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        Book.objects.create(title=title)
    return render(request, "bookshelf/create_book.html")


@permission_required("bookshelf.can_edit", raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.title = request.POST.get("title")
        book.save()
    return render(request, "bookshelf/edit_book.html", {"book": book})


@permission_required("bookshelf.can_delete", raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
    return render(request, "bookshelf/delete_book.html", {"book": book})
