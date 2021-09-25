from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='post-index'),
    path('lista/', views.lista, name='post-lista'),
    path('lista/<slug:slug>', views.post, name='post-descricao')
]