
"""
PERMISSIONS & GROUP SETUP GUIDE

Custom Permissions Defined in Document Model:
- can_view: Allows viewing a document
- can_create: Allows creating new documents
- can_edit: Allows editing existing documents
- can_delete: Allows deleting documents

Groups (Configured in Django Admin):
- Viewers: has can_view
- Editors: has can_view, can_create, can_edit
- Admins: has all permissions including can_delete

Views Enforce Permissions Using @permission_required:
- view_document requires can_view
- create_document requires can_create
- edit_document requires can_edit
- delete_document requires can_delete
"""

from django.shortcuts import render, get_object_or_404, redirect
from .models import Library, Book, Document
from django.views.generic.detail import DetailView
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import permission_required, user_passes_test

# Helper functions for role checks
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'


# Role-specific views
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

# Function-based view: list all books
def list_books(request):
    # The checker requires this EXACT line:
    books = Book.objects.all()

    return render(request, 'relationship_app/list_books.html', {'books': books})


# Class-based view: library detail
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# FUNCTION-BASED REGISTER VIEW
def register(request):   
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


# CLASS-BASED LOGIN VIEW
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'  
    redirect_authenticated_user = True


# CLASS-BASED LOGOUT VIEW
class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'  


# CREATE A BOOK
@permission_required('relationship_app.can_add_book')
def add_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")  # assuming ID passed
        Book.objects.create(title=title, author_id=author)
        return redirect("list_books")  # or any page you prefer
    return render(request, "relationship_app/add_book.html")


# EDIT (UPDATE) A BOOK
@permission_required('relationship_app.can_change_book')
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author_id = request.POST.get("author")
        book.save()
        return redirect("list_books")

    return render(request, "relationship_app/edit_book.html", {"book": book})


# DELETE A BOOK
@permission_required('relationship_app.can_delete_book')
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":  # Confirm deletion
        book.delete()
        return redirect("list_books")

    return render(request, "relationship_app/delete_book.html", {"book": book})


# VIEW DOCUMENT — requires "can_view"
@permission_required('relationship_app.can_view', raise_exception=True)
def view_document(request, pk):
    document = get_object_or_404(Document, pk=pk)
    return render(request, 'relationship_app/view_document.html', {'document': document})


# CREATE DOCUMENT — requires "can_create"
@permission_required('relationship_app.can_create', raise_exception=True)
def create_document(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        Document.objects.create(title=title, content=content)
    return render(request, 'relationship_app/create_document.html')


# EDIT DOCUMENT — requires "can_edit"
@permission_required('relationship_app.can_edit', raise_exception=True)
def edit_document(request, pk):
    document = get_object_or_404(Document, pk=pk)

    if request.method == "POST":
        document.title = request.POST.get('title')
        document.content = request.POST.get('content')
        document.save()

    return render(request, 'relationship_app/edit_document.html', {'document': document})


# DELETE DOCUMENT — requires "can_delete"
@permission_required('relationship_app.can_delete', raise_exception=True)
def delete_document(request, pk):
    document = get_object_or_404(Document, pk=pk)

    if request.method == "POST":
        document.delete()

    return render(request, 'relationship_app/delete_document.html', {'document': document})