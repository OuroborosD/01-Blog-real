from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models  import Post, Comentario
from .forms import ComentarioForm

# Create your views here.

def post(request, slug):
    post_descricao = Post.objects.get(slug=slug)
    id = int(post_descricao.pk)

    if request.method == 'POST':
        #form_comentario = request.POST
        #Comentario.objects.create(autor=form_comentario['autor'], 
        #                          comentario=form_comentario['comentario'],
        #                           post_id = Post.objects.get(slug=slug))#o objeto de onde vem a Oé Post
        
        form_post = ComentarioForm(request.POST)

        if form_post.is_valid():
            print(form_post.cleaned_data['autor'])
            Comentario.objects.create(autor= form_post.cleaned_data['autor'], 
                                  comentario=form_post.cleaned_data['comentario'],
                                   post_id = Post.objects.get(slug=slug))#o objeto de onde vem a Oé Post
            
        
        return HttpResponseRedirect(f'/lista/{slug}')
    
    form = ComentarioForm()

    comment = Comentario.objects.filter(post_id= id)# para mostrar todos os compentarios do post.
    tags = post_descricao.tags.all()
    context ={
        'post':post_descricao,
        'post_tags':tags,
        'comments':comment,
        'form': form
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


