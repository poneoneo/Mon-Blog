from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext as _

class Manager(BaseUserManager):

    def create_user(self,email, password, **extra_fields):
    #Impossible de creer un utilisateur sans renseigner un email
        if email is None :
            raise ValueError(_("Vous devez entrer une adresse email"))
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    

    def create_superuser(self, email, password, **extra_fields):
    #On donne les droit par default pour un superutilisateur
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

    #On verifie si le super utilisatur a les roles requis pour l'etre si non renvoie un errreur
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Un Super utilisateur doit avoir : is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Un Super utilisateur doit avoir: is_superuser=True.'))

    #Si oui on renvoie l'utilisateur renvoye par la methode create_user
        return self.create_user(email, password, **extra_fields)
