from django.shortcuts import get_object_or_404
from rest_framework import status, views
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer


class BookListCreateAPIView(views.APIView):
    """Book model list or register api class"""

    def get(self, request, *args, **kwargs):
        """Book model list handler"""

        # Book model list
        book_list = Book.objects.all()
        # create serialized object
        serializer = BookSerializer(instance=book_list, many=True)
        # return Response object
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """Book model register handler"""

        # create serializer object
        serializer = BookSerializer(data=request.data)
        # validation
        serializer.is_valid(raise_exception=True)
        # register object
        serializer.save()
        # return Response object
        return Response(serializer.data, status.HTTP_201_CREATED)


class BookRetrieveUpdateDestroyAPIView(views.APIView):
    pass


