from __future__ import unicode_literals

from django.db import models
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# no need to migrate when changing / updating the model manager.
class UserManager(models.Manager):
    def register(self, postData):
        errors = []

        if not postData['first_name']:
            errors.append('No first name entered.  Please enter a first name')
        if not postData['last_name']:
            errors.append('No last name entered.  Please enter a last name')
                #--- end of name checks --
        if not postData['email']:
            errors.append('No email entered.  Please enter an email')
        elif not EMAIL_REGEX.match(postData['email']):
            errors.append('No email entered.  Please enter a valid email')
        #if this email filter comes back empty it will resutl in a return of false = meaning email not in system already.
        elif self.filter(email=postData['email']):
            errors.append('This email address is already in use.  Please enter a new, valid email')
        #--- end of email checks --
        if not postData['password']:
            errors.append('Please enter a password')
        elif len(postData['password']) < 8:
            errors.append('Password is not long enough.  Must be at least 8 characters')
        elif postData['password'] != postData['confirm_password']:
            errors.append('Passwords must match')

        validation_response = {}

        if errors:
            validation_response['added'] = False
            validation_response['errors'] = errors
        else:
            validation_response['added'] = True #Jack has different bcrpyt syntax
            validation_response['new_user'] = self.create(first_name=postData['first_name'], last_name=postData['last_name'], email=postData['email'], password=bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()))

        return validation_response
        # print validation_response['new_user']
    def login(self, postData):
        user = User.objects.filter(email=postData['email'])

# migrate if adding models.__field__
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    #email = models.EmailField()
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    objects = UserManager()
