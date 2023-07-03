from django.db import models
from user.models import CustomUser


class Post(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title
