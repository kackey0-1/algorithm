from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    """Book Model Serializer"""

    class Meta:
        # identify target class
        model = Book
        # identify not in-use field
        exclude = ['created_at']

