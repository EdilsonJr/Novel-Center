from django.db import models
from categorias.models import Categoria
from django.contrib.auth.models import User
from django.utils import timezone


class Novel(models.Model):
    titulo = models.CharField(max_length=50, verbose_name='Título')
    autor = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    data = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(verbose_name='Descrição')
    excerto = models.TextField()
    qdt_volumes = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, blank=True, null=True)
    imagem = models.ImageField(upload_to='novel_img/%Y/%m/%d')
    wallpaper = models.ImageField(upload_to='novel_wall/%Y/%m/%d')
    publicado = models.BooleanField(default=False)
    outros_titulos = models.CharField(max_length=150)
    escritor = models.CharField(max_length=50)
    ilustrador = models.CharField(max_length=50)
    status = models.CharField(max_length=25)

    def __str__(self):
        return self.titulo


class Volume(models.Model):
    novel_vol = models.ForeignKey(Novel, on_delete=models.CASCADE)
    vol_vol = models.CharField(max_length=50)
    titulo_vol = models.CharField(max_length=50)
    capa_vol = models.ImageField(upload_to='vol_capa/%Y/%m/%d')
    num_vol = models.IntegerField()
    descriacao_vol = models.TextField()
    data_vol = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo_vol


class Capitulo(models.Model):
    volume_cap = models.ForeignKey(Volume, on_delete=models.CASCADE)
    titulo_cap = models.CharField(max_length=100)
    conteudo_cap = models.TextField()
    data_cap = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo_cap
