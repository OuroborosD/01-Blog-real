from django.shortcuts import render

from .models  import Post

# Create your views here.

def post(request, slug):
    post_descricao = Post.objects.get(slug=slug)
    context ={
        'post':post_descricao
    }
    return render(request, 'post/post.html',context)


def index(request):
    posts_recentes = Post.objects.all()
    context ={
        'posts': posts_recentes
    }
    return render(request, 'post/index.html', context)

def lista(request):
    pass