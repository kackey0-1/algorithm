import uuid

from django.db import models


class EmojiLog(models.Model):
    """Emoji Log model"""

    class Meta:
        db_table = 'emoji_log'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    text = models.CharField(verbose_name='テキスト', max_length=50)
    color = models.CharField(verbose_name='カラー', max_length=10)
    name = models.CharField(verbose_name='ファイル名', max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Author(models.Model):
    """Author model"""

    class Meta:
        db_table = 'author'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    name = models.CharField(verbose_name='著者名', max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Book(models.Model):
    """Book model"""

    class Meta:
        db_table = 'book'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(verbose_name='タイトル', max_length=20)
    price = models.IntegerField(verbose_name='価格', null=True)
    author = models.ManyToManyField(Author, verbose_name='著者', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title










