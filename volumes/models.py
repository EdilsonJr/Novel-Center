from django.db import models
from novel.models import Novel
from django.utils import timezone


class Volume(models.Model):
    novel_vol = models.ForeignKey(Novel, on_delete=models.CASCADE)
    titulo_vol = models.CharField(max_length=50)
    capa_vol = models.ImageField(upload_to='vol_capa/%Y/%m/%d')
    num_vol = models.IntegerField()
    descriacao_vol = models.TextField()
    data_vol = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo_vol
