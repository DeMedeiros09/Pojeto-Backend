from django.db import models

# Create your models here.

class Categoria(models.Model):
    categoria = models.TextField(blank=True, null=True)

class Autor(models.Model):
    autor = models.TextField(blank=True, null=True)

class Receita(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    ingredientes = models.TextField(blank=True, null=True)
    modo_de_preparo = models.TextField(blank=True, null=True)
    tempo_de_preparo = models.IntegerField(help_text='tempo em minutos')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='categoria')
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE,related_name='autor')
    data_de_criacao = models.DateField(help_text="Data de criacao")
    publica_privada = models.BooleanField(default=True, help_text='indica se a receita eh public')

class Usuario(models.Model):
    usuario = models.TextField(blank=True, null=True)

class Avaliacao(models.Model):
    receita = models.ForeignKey(Receita, on_delete=models.CASCADE,related_name='receitas')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE,related_name='usuario')
    nota = models.IntegerField(blank=True, null=True, help_text='nota da receita')
    comentario = models.TextField(blank=True, null=True)

