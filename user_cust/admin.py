from django.contrib import admin
from .models import  Blogger 
from django.contrib.auth.admin import UserAdmin

class BloggerAdmin(admin.ModelAdmin):
    model = Blogger
    list_display = ("username", "email", "is_staff", "is_superuser", "date_joined")
    ordering = ["username"]
    verbose_name = "Blogger"    


admin.site.register(Blogger, BloggerAdmin)


