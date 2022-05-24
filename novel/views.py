from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from .models import Novel


class NovelIndex(ListView):
    model = Novel
    template_name = 'novel/index.html'


class NovelBusca(NovelIndex):
    pass


class NovelCategoria(NovelIndex):
    pass


class NovelDetalhes(UpdateView):
    pass