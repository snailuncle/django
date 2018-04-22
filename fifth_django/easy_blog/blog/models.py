from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Article(models.Model):
    "文章数据库"
    title=models.CharField(max_length=70)
    body=models.TextField()
    created_time=models.DateTimeField()
    

