from django.db import models


class UserNormal(models.Model):
    nome = models.CharField(max_length=100)
    username = models.CharField(max_length=20, unique=True)
    email = models.CharField(max_length=50, unique=True)
    senha = models.CharField(max_length=50)
    telefone = models.CharField(max_length=20)
    pais = models.CharField(max_length=40)
    foto = models.ImageField(upload_to='user_foto/%Y/%m/%d')

    def __str__(self):
        return self.nome
