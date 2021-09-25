from django.shortcuts import render

from .models  import Post

# Create your views here.

def post(request, slug):
    post_descricao = Post.objects.get(slug=slug)
    tags = post_descricao.tags.all()
    context ={
        'post':post_descricao,
        'post_tags':tags
    }
    return render(request, 'post/post.html',context)


def index(request):
    posts_recentes = Post.objects.all()
    context ={
        'posts': posts_recentes
    }
    return render(request, 'post/index.html', context)

def lista(request):
    return render(request,'post/lista.html')