from django.shortcuts import render, redirect
from .models import Articles
from user_cust.models import Blogger
from django.contrib.auth import get_user_model

def home(request):
    

    return render(request, "articles/home.html")