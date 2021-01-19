# Generated by Django 2.2.5 on 2021-01-19 14:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20, verbose_name='タイトル')),
                ('price', models.IntegerField(null=True, verbose_name='価格')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2021, 1, 19, 14, 39, 10, 76625, tzinfo=utc))),
            ],
            options={
                'db_table': 'book',
            },
        ),
    ]
