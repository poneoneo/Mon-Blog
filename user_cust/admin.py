from django.contrib import admin
from .models import CustomUser, Blogger 
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("username", "email", "is_staff", "is_superuser", "first_name", "date_joined")
    ordering = ["email"]

admin.site.register(CustomUser ,CustomUserAdmin)
admin.site.register(Blogger)


