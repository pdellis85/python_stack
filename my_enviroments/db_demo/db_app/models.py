from django.db import models

# Create your models here.

# -  Create a user table!
#       -  Users have usernames, passwords, created_at and updated_at

class User(models.Model):
    username = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
