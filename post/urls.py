from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('lista/', views.lista),
    path('lista/<slug:slug>', views.post, name='post-descricao')
]