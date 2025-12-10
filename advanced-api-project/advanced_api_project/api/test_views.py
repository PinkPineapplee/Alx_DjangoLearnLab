# Explain that you're testing CRUD, filters, search, ordering
# Mention login required for create/update/delete.
# Run test command: python manage.py test api

from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Author, Book
from django.contrib.auth.models import User



class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="password123")

        # Create authors
        self.author1 = Author.objects.create(name="J.K. Rowling")
        self.author2 = Author.objects.create(name="George R.R. Martin")

        # Create books
        self.book1 = Book.objects.create(title="Harry Potter", publication_year=1997, author=self.author1)
        self.book2 = Book.objects.create(title="Game of Thrones", publication_year=1996, author=self.author2)

        # API client
        self.client = APIClient()



    def test_list_books(self):
        url = reverse('book-list')  # Make sure your URL name matches
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_book_authenticated(self):
        self.client.login(username="testuser", password="password123")
        url = reverse('book-list')
        data = {
            "title": "New Book",
            "publication_year": 2025,
            "author": self.author1.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_update_book_authenticated(self):
        self.client.login(username="testuser", password="password123")
        url = reverse('book-detail', args=[self.book1.id])
        data = {"title": "Updated Harry Potter", "publication_year": 1997, "author": self.author1.id}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Harry Potter")

    def test_delete_book_authenticated(self):
        self.client.login(username="testuser", password="password123")
        url = reverse('book-detail', args=[self.book2.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)


    def test_search_books(self):
        url = reverse('book-list') + "?search=Harry"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_filter_books_by_author(self):
        url = reverse('book-list') + f"?author={self.author2.id}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books_by_publication_year(self):
        url = reverse('book-list') + "?ordering=publication_year"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], "Game of Thrones")  # 1996 first
