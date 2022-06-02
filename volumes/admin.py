from django.contrib import admin
from .models import Volume


class VolumeAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo_vol', 'novel_vol', 'num_vol')


admin.site.register(Volume, VolumeAdmin)
