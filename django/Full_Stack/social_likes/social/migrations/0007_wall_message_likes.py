# Generated by Django 2.2 on 2020-08-23 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0006_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='wall_message',
            name='likes',
            field=models.ManyToManyField(related_name='likes', to='social.User'),
        ),
    ]
