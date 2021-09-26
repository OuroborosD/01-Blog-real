from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE

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

    def __str__(self) -> str:
        return self.title
   


class Comentario(models.Model):
    autor= models.CharField(max_length=50)
    comentario = models.TextField()
    post_id = models.ForeignKey(Post, on_delete=CASCADE, null=True)

    def __str__(self) -> str:
        return self.autor
