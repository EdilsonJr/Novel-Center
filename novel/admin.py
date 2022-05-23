from django.contrib import admin
from .models import Novel


class NovelAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'autor', 'data', 'categoria', 'publicado')
    list_editable = ('publicado',)
    list_display_links = ('id', 'titulo')


admin.site.register(Novel, NovelAdmin)