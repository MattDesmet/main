from __future__ import unicode_literals

from django.db import models

from ..users.models import User
# Create your models here.
class Course(models.Model):
        name = models.CharField(max_length=255)
        description = models.TextField()
        users = models.ManyToManyField(User, related_name='courses')
        created_at = models.DateField(auto_now_add=True)
        updated_at = models.DateField(auto_now=True)
