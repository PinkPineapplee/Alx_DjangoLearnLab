from django.urls import path, include
from . import views
from .views import list_books, login_view, logout_view, register_view

app_name = 'relationship_app'

urlpatterns = [
    path('books/', views.list_books, name='list_books'),  # Function-based view
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # Class-based view
    path('relationship_app/', include('relationship_app.urls', namespace='relationship_app')),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),

]
