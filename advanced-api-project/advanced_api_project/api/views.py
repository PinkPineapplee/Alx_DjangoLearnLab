from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer


# Create your views here.
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# DetailView -> GET /books/<pk>/
# Allows public read-only access.
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# CreatView -> POST /books/
# Only authenticated users can create a new book.
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Custom behavior -> attach the user or modify data before saving(optional)
    def perform_create(self, serializer):
        # Example: You can hook extra logic here
        serializer.save()        

#UpdateView -> PUT/PATCH / books/<pk>/
# Only authenticated users can update.
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        #Extra hooks can be added here
        serializer.save()
        # automatically force publication_year to int if needed
        pub_year = int(self.request.data.get("publication_year", 0))
        serializer.save(publication_year=pub_year)

 # DeleteView -> DELETE / books/<pk>/
 # Only authenticated users can delete.
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    permission_classes = [permissions.IsAuthenticated]
