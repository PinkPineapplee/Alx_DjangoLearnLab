# api/serializers.py
from rest_framework import serializers
from .models import Book  # Import your Book model

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # Include all fields from the Book model
