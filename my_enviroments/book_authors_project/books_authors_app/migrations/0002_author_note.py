# Generated by Django 2.2 on 2020-08-17 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='note',
            field=models.CharField(default='old books', max_length=255),
            preserve_default=False,
        ),
    ]
