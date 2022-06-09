from django.contrib import admin
from .models import UserNormal


class UserNormalAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'nome', 'pais')
    list_display_links = ('id', 'username')


admin.site.register(UserNormal, UserNormalAdmin)
