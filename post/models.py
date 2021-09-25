from django.db import models
from django.db.models.base import Model

# Create your models here.

class Tags(models.Model):
    nome = models.CharField(max_length=30)
    
    class Meta:
        verbose_name_plural = "Tags"
    
    def __str__(self):
        return  self.nome


class Post(models.Model):
    title = models.CharField(max_length=50)
    criacao = models.DateTimeField(auto_now=True)
    autor = models.CharField(max_length=50)
    texto = models.TextField()
    slug = models.SlugField(default='',null=False,blank=True, db_index=True)
    tags = models.ManyToManyField(Tags, default='S/T')

    