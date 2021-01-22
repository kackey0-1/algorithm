from rest_framework import serializers

from .models import Book, EmojiLog


class EmojiLogSerializer(serializers.ModelSerializer):
    """Emoji Log Model Serializer"""

    class Meta:
        # identify target class
        model = EmojiLog
        # identify not in-use field
        exclude = ['created_at', 'updated_at']


class BookSerializer(serializers.ModelSerializer):
    """Book Model Serializer"""

    class Meta:
        # identify target class
        model = Book
        # identify not in-use field
        exclude = ['created_at']

