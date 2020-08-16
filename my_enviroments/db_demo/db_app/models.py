from django.db import models

# Create your models here.

# -  Create a user table!
#       -  Users have usernames, passwords, created_at and updated_at

class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# -  Create a Message_Post table!
#       -  Message_Post include message contents, user_who_posted, created_at and updated_at 

class Message_Post(models.Model):
    content = models.CharField(max_length=255)
    poster = models.ForeignKey(User, related_name=)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# -  Create a Likes table!
#       -  Users should have the ability to 'like' a Message_post 

class Like(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)