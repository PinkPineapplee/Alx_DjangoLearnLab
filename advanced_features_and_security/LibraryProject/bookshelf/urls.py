from django.urls import path
from . import views

urlpatterns = [
    path("book-list/", views.book_list, name="book_list"),
    path("books/", views.books, name="books"),
    path("error/", views.raise_exception, name="raise_exception"),
    path("example-form/", views.example_form_view, name="example_form"),
]
