from django.db import models
from time import gmtime, strftime
from datetime import *
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def registration_validator(self, postData):
        errors = {}
        #email validity
        email = User.objects.filter(email=postData['email'])
        if email:
            errors['unique_email'] = "Email already in use."
        if not EMAIL_REGEX.match(postData['email']):
            errors['validity'] = "Invalid email address format."
        #first and last name validity
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name should contain at least 2 characters."
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name should contain at least 2 characters."
        #username validity
        username = User.objects.filter(username=postData['username'])
        if username:
            errors['unique_username'] = "Username has already been taken."
        if len(postData['username']) < 5:
            errors['username_len'] = "Username must be at least 5 characters long."
        #password validity
        if postData['password'] != postData['confirmed_password']:
            errors['password_match'] = "Passwords do not match, try again."
        if len(postData['password']) < 8 and len(postData['confirmed_password']) < 8:
            errors['password_length'] = "Password must be at least 8 characters."
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Post(models.Model):
    text_content = models.CharField(max_length=255)
    added_by = models.ForeignKey(User, related_name= "posts", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)