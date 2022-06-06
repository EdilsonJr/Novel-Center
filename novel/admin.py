from django.contrib import admin
from . import models
from django_summernote.admin import SummernoteModelAdmin
from .models import Novel


class VolumeInline(admin.TabularInline):
    model = models.Volume
    extra = 1


class NovelAdmin(SummernoteModelAdmin):
    list_display = ('id', 'titulo', 'autor', 'data', 'categoria', 'publicado')
    list_editable = ('publicado',)
    list_display_links = ('id', 'titulo')
    summernote_fields = ('excerto',)
    inlines = [
        VolumeInline
    ]


class VolumeAdmin(SummernoteModelAdmin):
    list_display = ('id', 'vol_vol', 'novel_vol', 'titulo_vol')
    list_display_links = ('id', 'vol_vol')


admin.site.register(Novel, NovelAdmin)
admin.site.register(models.Volume, VolumeAdmin)
# admin.site.register(models.Capitulo)

