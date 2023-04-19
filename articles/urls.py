from django.urls import path
from . import views


urlpatterns =[
    path("accueil/",views.home, name = "home"),
    path("accueil/hello",views.ArticlesList.as_view(), name = "articles-list"),
    

]