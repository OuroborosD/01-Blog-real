from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models  import Post, Comentario
from .forms import ComentarioForm

# Create your views here.

def post(request, slug):
    post_descricao = Post.objects.get(slug=slug)#pega todos os ativutos do post com o slug igual
    id = int(post_descricao.pk)

    if request.method == 'POST':
        #form_comentario = request.POST
        #Comentario.objects.create(autor=form_comentario['autor'], 
        #                          comentario=form_comentario['comentario'],
        #                           post_id = Post.objects.get(slug=slug))#o objeto de onde vem a Oé Post
        
        # se recebeu um post, peega os dados do post e coloca na varial form_post
        form_post = ComentarioForm(request.POST)

        if form_post.is_valid():#verifica se os campos do formulçario são validos
            print(form_post.cleaned_data['autor'])
            Comentario.objects.create(autor= form_post.cleaned_data['autor'],  #salva o post no database.
                                  comentario=form_post.cleaned_data['comentario'],
                                   post_id = Post.objects.get(slug=slug))#o objeto de onde vem a Oé Post
            
        
            return HttpResponseRedirect(f'/lista/{slug}')#redireciana para a pagina, ccaso de certo.
    
    else:
        form_post = ComentarioForm()

    comment = Comentario.objects.filter(post_id= id)# para mostrar todos os compentarios do post.
    tags = post_descricao.tags.all()
    context ={
        'post':post_descricao,
        'post_tags':tags,
        'comments':comment,
        'forms': form_post
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


