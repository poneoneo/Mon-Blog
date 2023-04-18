from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import uuid

class CustomUser(AbstractUser):
    pass


class Blogger(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL, primary_key = True, blank = False, on_delete = models.CASCADE)
    profile_pic = models.ImageField(upload_to="profile", blank = True, null = True )
    username = models.CharField(max_length = 150)
    password = models.CharField(max_length = 10)
    email = models.EmailField()
    bio = models.CharField(max_length = 200, default = f"Hello Je m'appelle {username} et j'ecris des articles sur mon apprentissage du framework Django")

    def __str__(self):
        return self.username


