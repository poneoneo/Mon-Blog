from django.utils.text import slugify
from django.conf import settings
from django.db import models
import uuid
import datetime
from user_cust.models import Blogger

class Articles(models.Model):

    blogger= models.ForeignKey(Blogger, on_delete=models.CASCADE, limit_choices_to = {"is_staff":True},primary_key = False, default = "" )
    id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4)
    
    title = models.CharField(max_length = 200)
    slug = models.SlugField(default="", editable=False, max_length=200, null = False)
    body  = models.TextField(blank=False, null = False, default="")
    created_at = models.DateTimeField(auto_now=datetime.datetime.now)
    update_at = models.DateTimeField(auto_now_add=datetime.datetime.now)
    image = models.ImageField(upload_to = "article_images", blank = True)
    nb_articles =models.IntegerField(default = 0 ) 
  

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value=value, allow_unicode=True)
        nb_articles += 1
        super().save(*args, **kwargs)

    def get_absolute_url(self, *args, **kwargs):
        pass

    def published_recently(self):
        pass

