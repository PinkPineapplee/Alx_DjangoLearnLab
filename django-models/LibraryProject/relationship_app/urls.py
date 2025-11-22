from django.urls import path, include
from . import views
from .views import list_books

app_name = 'relationship_app'

urlpatterns = [
    path('books/', views.list_books, name='list_books'),  # Function-based view
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # Class-based view
    path('relationship_app/', include('relationship_app.urls', namespace='relationship_app')),

]
