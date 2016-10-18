from __future__ import unicode_literals
from django.db import models
import bcrypt

import re
email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
#found a name regex from online
name_regex = re.compile(r'^[A-Z][-a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def login(self, form_data):
        print("Validating login")
        # retrieve the user from database using email
        user = User.objects.filter(email=form_data['email'])
        if user:
            user = user[0]
            if bcrypt.checkpw(form_data['pw'].encode(), user.pw_hash.encode()):
                print("passwords match")
                return (True, user)
        return (False, "Invalid email or password")

    def register(self, form_data):
        # Validation portion. Pushes all errors to an array that is returned if there are errors
        errors = []
        if len(form_data['email']) == 0:
            errors.append("Email is required")
        if not email_regex.match(form_data['email']):
            errors.append("Invalid Email")

        # checks if there were any errors
        if len(errors) is not 0:
            return (False, errors)
        else:
            print("passed validations")
            #print(form_data['pw'].encode())
            #create the hashed password using bcrypt. Remember to encode
            pw_hash = bcrypt.hashpw(form_data['pw'].encode(), bcrypt.gensalt().encode())
            # create() method in objects returns newly entered entry in your db
            user = User.objects.create(email=form_data['email'], first_name=form_data['first_name'], last_name=form_data['last_name'], pw_hash=pw_hash)
            return (True, user)

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    pw_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
