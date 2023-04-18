from django.db import models
from .manager import Manager
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils.translation import gettext as _
import uuid

class CustomUser(AbstractUser):
    """ 
    REQUIRED_FIELDS
     doit contenir les champs obligatoire pour un utilisateur 
    sauf celui ecrit dans USERNAME_FIELD ou password car il faudra fournir des valeurs pour ces champs
    consulter la doc https://docs.djangoproject.com/fr/4.1/topics/auth/customizing/#django.contrib.auth.models.CustomUser.REQUIRED_FIELDS
     """
    username = None
    email = models.EmailField(_("Adresse Email"), unique=True)

    objects = Manager()

    USERNAME_FIELD = "email"
   
    REQUIRED_FIELDS = []
    


class Blogger(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL, primary_key = True, blank = False, on_delete = models.CASCADE)
    profile_pic = models.ImageField(upload_to="profile", blank = True, null = True )
    username = models.CharField(max_length = 150)
    bio = models.CharField(max_length = 200, default = f"Hello Je m'appelle {username} et j'ecris des articles sur mon apprentissage du framework Django")

    
    def __str__(self):
        return self.username


