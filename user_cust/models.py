from django.db import models
from .manager import Manager
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils.translation import gettext as _
import uuid

class Blogger(AbstractUser):

    email = models.EmailField(_("Adresse Email"), unique=True, primary_key = True)
    username = models.CharField(max_length = 200, default = "" )

    # info du blogger
    profile_pic = models.ImageField(upload_to="profile", blank = True, null = True)
    bio = models.CharField(max_length = 200, default = "")

    def __str__(self):
        return self.username    
   
    """ 
    REQUIRED_FIELDS
        doit contenir les champs obligatoire pour un utilisateur 
    sauf celui ecrit dans USERNAME_FIELD ou password car il faudra fournir des valeurs pour ces champs
    consulter la doc https://docs.djangoproject.com/fr/4.1/topics/auth/customizing/#django.contrib.auth.models.CustomUser.REQUIRED_FIELDS
    """
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username",]
    objects = Manager()
    



    


