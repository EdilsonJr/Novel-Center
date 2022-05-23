from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


class NovelIndex(ListView):
    pass


class NovelBusca(NovelIndex):
    pass


class NovelCategoria(NovelIndex):
    pass


class NovelDetalhes(UpdateView):
    pass