from django.urls import path
from . import views

urlpatterns = [
    path('', views.NovelIndex.as_view(), name='index'),
    path('categoria/<str:categoria>', views.NovelCategoria.as_view(), name='novel_categoria'),
    path('busca/', views.NovelBusca.as_view(), name='novel_busca'),
    path('post/<int:pk>', views.NovelDetalhes.as_view(), name='novel_detalhes'),
]
