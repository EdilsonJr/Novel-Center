from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from .models import Novel
from django.db.models import Q, Count, Case, When
from comentarios.forms import FormComentario


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

    def get_queryset(self):
        qs = super().get_queryset()

        termo = self.request.GET.get('termo')

        if not termo:
            return qs

        qs = qs.filter(
            Q(titulo__icontains=termo) |
            Q(conteudo__icontains=termo) |
            Q(excerto__icontains=termo) |
            Q(categoria__nome_cat__iexact=termo) |
            Q(autor__username__iexact=termo)
        )

        return qs


class NovelCategoria(NovelIndex):
    template_name = 'novel/novel_categoria.html'

    def get_queryset(self):
        qs = super().get_queryset()

        categoria = self.kwargs.get('categoria', None)

        if not categoria:
            return qs

        qs = qs.filter(categoria__nome_cat__iexact=categoria)

        return qs


class NovelDetalhes(UpdateView):
    template_name = 'novel/novel_detalhes.html'
    model = Novel
    form_class = FormComentario
    context_object_name = 'novel'

