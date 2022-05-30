from django.forms import ModelForm
from .models import Comentario


class FormComentario(ModelForm):
    class Meta:
        model = Comentario
        fields = ('nome_comentario', 'email_comentario', 'comentario')
