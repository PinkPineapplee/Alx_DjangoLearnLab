Relationship Explanation

Author and Book have a one-to-many relationship.

This is implemented using a ForeignKey inside Book, pointing to Author.

In the serializer:

AuthorSerializer includes a nested BookSerializer.

The related_name="books" lets you access all books of an author using author.books.

Validation

BookSerializer.validate_publication_year() checks that:

The year is not in the future.

Raises a ValidationError if invalid.s