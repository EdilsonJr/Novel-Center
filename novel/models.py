from django.db import models
from categorias.models import Categoria
from django.contrib.auth.models import User
from django.utils import timezone


class Novel(models.Model):
    titulo = models.CharField(max_length=50, verbose_name='Título')
    autor = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    data = models.DateTimeField(default=timezone.now)
    conteudo = models.TextField()
    descricao = models.TextField()
    excerto = models.TextField()
    volume = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, blank=True, null=True)
    imagem = models.ImageField(upload_to='novel_img/%Y/%m/%d')
    wallpaper = models.ImageField(upload_to='novel_img/%Y/%m/%d')
    publicado = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
