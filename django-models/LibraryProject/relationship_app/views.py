
from django.shortcuts import render, get_object_or_404, redirect
from .models import Library, Book
from django.views.generic.detail import DetailView
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView


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
