from django.db import models
from django.db.models.base import Model

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    criacao = models.DateTimeField(auto_now=True)
    autor = models.CharField(max_length=50)
    texto = models.TextField()
    