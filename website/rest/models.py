from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Recording(models.Model):
      name = models.CharField(max_length=128)
      path = models.CharField(max_length=255)
      datetime = models.models.DateTimeField()
      insertTime = models.DateTimeField(auto_now_add=True)
      updateTime = models.DateTimeField(auto_now=True, null=True)
      user = models.ForeignKey(User)


class UserDetails(models.Model):
    user = models.ForeignKey(User)
    facebookID = models.CharField(max_length=64)