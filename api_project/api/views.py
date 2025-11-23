# api/views.py
from rest_framework import generics, viewsets, permissions
from .models import Book
from .serializers import BookSerializer

# Existing list view
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# New ViewSet for full CRUD
class BookViewSet(viewsets.ModelViewSet):
    """
    Provides list, create, retrieve, update, and destroy actions for Book model.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated] 
