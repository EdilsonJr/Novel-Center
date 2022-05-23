from django.contrib import admin
from .models import Novel
from django_summernote.admin import SummernoteModelAdmin


class NovelAdmin(SummernoteModelAdmin):
    list_display = ('id', 'titulo', 'autor', 'data', 'categoria', 'publicado')
    list_editable = ('publicado',)
    list_display_links = ('id', 'titulo')
    summernote_fields = ('conteudo',)


admin.site.register(Novel, NovelAdmin)