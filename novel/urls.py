from django.urls import path
from . import views

urlpatterns = [
    path('', views.NovelIndex.as_view(), name='index'),
    path('categoria/<str:categoria>', views.NovelCategoria.as_view(), name='novel_categoria'),
    path('busca/', views.NovelBusca.as_view(), name='novel_busca'),
    path('novel/<slug>', views.NovelDetalhes.as_view(), name='novel_detalhes'),
    path('volume/<int:pk>', views.VolumeDetalhes.as_view(), name='volume_detalhes'),
    path('capitulo/<int:pk>', views.CapituloDetalhes.as_view(), name='capitulo_detalhes'),
]
