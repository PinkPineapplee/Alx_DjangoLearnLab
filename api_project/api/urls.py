# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet
from rest_framework.authtoken.views import obtain_auth_token

# Initialize the router
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Existing list view
    path('books/', BookList.as_view(), name='book-list'),

    # Include router URLs for full CRUD operations
    path('', include(router.urls)),

    # Endpoint to obtain auth token
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
