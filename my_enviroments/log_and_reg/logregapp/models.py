from django.db import models
import re

# Create your models here.

# First Name - required; at least 2 characters; letters only
# Last Name - required; at least 2 characters; letters only
# Email - required; valid format
# Password - required; at least 8 characters; matches password confirmation


class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        # add keys and values to errors dictionary for each invalid field
        if len(postData['first_name']) < 2:
            errors["first_name"] = "Your first name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Your last name should be at least 2 characters"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        if len(postData['password']) < 8:
            errors["password"] = "Your password should be at least 8 characters"
        if postData["password"] != postData["confirm_password"]:
            errors["confirm_password"] = "Password and confirm password do not match"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
