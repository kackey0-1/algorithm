from django.shortcuts import get_object_or_404
from rest_framework import status, views
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer


class BookListCreateAPIView(views.APIView):
    """Book model list or register api class"""

    def get(self, request, *args, **kwargs):
        """Book model list handler"""

        # get Book model list
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
    """Book model detail, update, delete API class"""

    def get(self, request, pk, *args, **kwargs):
        """Book model detail handler"""

        # get Book object
        book = get_object_or_404(Book, pk=pk)
        # create serializer object
        serializer = BookSerializer(instance=book)
        # return Response object
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, request, pk, *args, **kwargs):
        """Book model update handler"""

        # get Book model
        book = get_object_or_404(Book, pk=pk)
        # create serializer object
        serializer = BookSerializer(instance=book, data=request.data, partial=True)
        # valiadtion
        serializer.is_valid(raise_exception=True)
        # save Book object
        serializer.save()
        # return Response object
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request, pk, *args, **kwargs):
        """Book model delete handler"""

        # get Book model
        book = get_object_or_404(Book, pk=pk)
        # delete Book model
        book.delete()
        # return Response object
        return Response(status=status.HTTP_204_NO_CONTENT)


