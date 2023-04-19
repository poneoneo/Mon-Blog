from django.shortcuts import render, redirect
from .models import Articles
from user_cust.models import Blogger
from django.contrib.auth import get_user_model
from django.views.generic.list import ListView
from django.utils import timezone as tz

User = get_user_model()
def home(request):
    return render(request, "articles/articles.html")

class ArticlesList(ListView):
    model = Articles
    paginated_by = 1
    # templates_name = "articles/articles_list.html"

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = tz.now()
        context["name"] = Blogger.objects.get(username = "O'neal Mboula")
      
        return context



    
