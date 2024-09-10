from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Categoria(models.Model):
    categoria = models.TextField(blank=True, null=True)


class Receita(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    ingredientes = models.TextField(blank=True, null=True)
    modo_de_preparo = models.TextField(blank=True, null=True)
    tempo_de_preparo = models.IntegerField(help_text='tempo em minutos')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    data_de_criacao = models.DateField(help_text="Data de criacao")
    publica_privada = models.BooleanField(default=True, )


class Avaliacao(models.Model):
    receita = models.ForeignKey(Receita, on_delete=models.CASCADE,)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE,)
    nota = models.IntegerField(blank=True, null=True,)
    comentario = models.TextField(blank=True, null=True)

