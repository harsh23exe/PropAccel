from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    user_id = models.IntegerField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    username = models.CharField(max_length=50, unique=True)

