from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Recieve(models.Model):
    message = models.TextField(blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
