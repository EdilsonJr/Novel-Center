from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from .models import Novel
from django.db.models import Q, Count, Case, When


class NovelIndex(ListView):
    model = Novel
    template_name = 'novel/index.html'
    context_object_name = 'novels'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by('-id').filter(publicado=True)
        qs = qs.annotate(
            qtd_comentarios=Count(
                Case(
                    When(comentario__publicado_comentario=True, then=1)
                )
            )
        )

        return qs


class NovelBusca(NovelIndex):
    template_name = 'novel/novel_busca.html'


class NovelCategoria(NovelIndex):
    template_name = 'novel/novel_categoria.html'


class NovelDetalhes(UpdateView):
    pass
