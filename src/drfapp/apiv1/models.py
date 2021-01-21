import uuid

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Author(models.Model):
    """Author model"""

    class Meta:
        db_table = 'author'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    name = models.CharField(verbose_name='著者名', max_length=20)
    created = models.DateTimeField(default=timezone.now())


class Book(models.Model):
    """Book model"""

    class Meta:
        db_table = 'book'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(verbose_name='タイトル', max_length=20)
    price = models.IntegerField(verbose_name='価格', null=True)
    author = models.ManyToManyField(Author, verbose_name='著者', blank=True)
    created_at = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.title










