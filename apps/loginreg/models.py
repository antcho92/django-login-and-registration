from __future__ import unicode_literals
from django.db import models


import re
email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
#found a name regex from online
name_regex = re.compile(r'^[A-Z][-a-zA-Z]+$')

# Create your models here.
class EmailManager(models.Manager):
    def login(self, form_data):
        print("Login validations")
        pass
    def register(self, form_data):
        errors = []
        if len(form_data['email']) == 0:
            errors.append("Email is required")
        if not email_regex.match(form_data['email']):
            errors.append("Invalid Email")
        if len(errors) is not 0:
            return (False, errors)
        else:
            User.objects.create(email=form_data['email'], first_name=form_data['first_name'], last_name=form_data['last_name'], pw_hash=form_data['pw'])
            return (True, user)

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    pw_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = EmailManager()
