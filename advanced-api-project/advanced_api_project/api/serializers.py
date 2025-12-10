from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    # Serializer for the Book mode
    # Includes custom validation for publication_year and borrowed_year
    class Meta:
        model = Book 
        fields = ['id', 'title','author', 'publication_year', 'borrowed_date']


# Custom validation to ensure publication_year is not in the future
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Pulication year cannot be in the future.")
        return value




class AuthorSerializer(serializers.ModelSerializer):
    # Nested serializer:
    # This will automatically fetch all books related to the author
    books = BookSerializer(many = True, read_only = True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']     