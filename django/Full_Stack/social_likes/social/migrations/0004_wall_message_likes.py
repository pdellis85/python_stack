# Generated by Django 2.2 on 2020-08-14 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='wall_message',
            name='likes',
            field=models.ManyToManyField(related_name='likes', to='social.User'),
        ),
    ]